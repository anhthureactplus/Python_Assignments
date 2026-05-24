import time
from typing import List

import pandas as pd

from text_classifier.evaluation.evaluator import Evaluator


class TextClassificationPipeline:
    """Run vectorizers + classifiers and compare results."""

    def __init__(self, vectorizers: List, classifiers: List):
        self.vectorizers = vectorizers
        self.classifiers = classifiers
        self.evaluator = Evaluator()

    def run(self, X_train, X_test, y_train, y_test) -> pd.DataFrame:
        results = []

        for vectorizer in self.vectorizers:
            X_train_vec = vectorizer.fit_transform(X_train)
            X_test_vec = vectorizer.transform(X_test)

            for classifier in self.classifiers:
                start_time = time.perf_counter()
                classifier.fit(X_train_vec, y_train)
                training_time = time.perf_counter() - start_time

                y_pred = classifier.predict(X_test_vec)
                metrics = self.evaluator.evaluate(y_test, y_pred)

                results.append({
                    "Vectorizer": vectorizer.name(),
                    "Model": classifier.name(),
                    "Accuracy": round(metrics["accuracy"], 4),
                    "F1-score": round(metrics["f1_score"], 4),
                    "Training Speed (s)": round(training_time, 4),
                })

        return pd.DataFrame(results)
