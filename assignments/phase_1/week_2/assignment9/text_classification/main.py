from text_classifier.data.loader import DatasetLoader
from text_classifier.models.logistic_regression import LogisticRegressionClassifier
from text_classifier.models.naive_bayes import NaiveBayesClassifier
from text_classifier.pipeline import TextClassificationPipeline
from text_classifier.vectorizers.bow import BoWVectorizer
from text_classifier.vectorizers.tfidf import TFIDFVectorizer


def main():
    print("Loading dataset...")
    loader = DatasetLoader()
    X_train, X_test, y_train, y_test = loader.load()

    vectorizers = [
        BoWVectorizer(),
        TFIDFVectorizer(),
    ]

    classifiers = [
        LogisticRegressionClassifier(),
        NaiveBayesClassifier(),
    ]

    pipeline = TextClassificationPipeline(vectorizers, classifiers)
    results = pipeline.run(X_train, X_test, y_train, y_test)

    print("\n=== COMPARISON RESULTS ===")
    print(results.to_string(index=False))


if __name__ == "__main__":
    main()
