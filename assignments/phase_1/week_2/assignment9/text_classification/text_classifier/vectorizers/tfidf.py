from sklearn.feature_extraction.text import TfidfVectorizer

from text_classifier.config import Config
from text_classifier.vectorizers.base import BaseVectorizer


class TFIDFVectorizer(BaseVectorizer):
    """TF-IDF vectorizer."""

    def __init__(self, max_features: int = Config.MAX_FEATURES):
        self.vectorizer = TfidfVectorizer(
    max_features=50000,
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.9,
    sublinear_tf=True,
    analyzer="word"
)

    def fit_transform(self, texts):
        return self.vectorizer.fit_transform(texts)

    def transform(self, texts):
        return self.vectorizer.transform(texts)

    def name(self) -> str:
        return "TF-IDF"
