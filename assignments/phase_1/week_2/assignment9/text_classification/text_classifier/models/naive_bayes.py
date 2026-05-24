from sklearn.naive_bayes import MultinomialNB

from text_classifier.models.base import BaseClassifier


class NaiveBayesClassifier(BaseClassifier):
    """Multinomial Naive Bayes classifier."""

    def __init__(self):
        self.model = MultinomialNB()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self

    def predict(self, X_test):
        return self.model.predict(X_test)

    def name(self) -> str:
        return "Naive Bayes"
