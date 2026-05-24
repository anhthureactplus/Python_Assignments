from sklearn.feature_extraction.text import CountVectorizer

from text_classifier.config import Config
from text_classifier.vectorizers.base import BaseVectorizer


class BoWVectorizer(BaseVectorizer):
    """Bag of Words vectorizer."""

    def __init__(self, max_features: int = Config.MAX_FEATURES):
        self.vectorizer = CountVectorizer(max_features=max_features)

    def fit_transform(self, texts):
        return self.vectorizer.fit_transform(texts)

    def transform(self, texts):
        return self.vectorizer.transform(texts)

    def name(self) -> str:
        return "BoW"
