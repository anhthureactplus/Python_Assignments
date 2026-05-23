from tfidf.config import TFIDFConfig
from tfidf.utils import lowercase, build_vocab


class TFIDFVectorizer:
    """
    Vectorizer chính — điều phối build vocab và tính TF-IDF matrix.
    """

    def __init__(self):
        self.vocab: dict[str, int] = {}

    def fit(self, documents: list[str], config: TFIDFConfig) -> "TFIDFVectorizer":
        processed = [lowercase(d) for d in documents] if config.lowercase else documents
        self.vocab = build_vocab(processed)
        self._config = config
        return self

    def transform(self, documents: list[str]) -> list[list[float]]:
        processed = [lowercase(d) for d in documents] if self._config.lowercase else documents
        return self._config.strategy.compute_matrix(processed, self.vocab)

    def fit_transform(
        self, documents: list[str], config: TFIDFConfig
    ) -> list[list[float]]:
        return self.fit(documents, config).transform(documents)
