from sklearn.linear_model import LogisticRegression

from text_classifier.models.base import BaseClassifier


class LogisticRegressionClassifier(BaseClassifier):
    """Logistic Regression classifier."""

    def __init__(self):
        self.model = LogisticRegression(
    max_iter=5000,
    C=4.0,
    solver="saga"
)
    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self

    def predict(self, X_test):
        return self.model.predict(X_test)

    def name(self) -> str:
        return "Logistic Regression"
