from bow.config import BoWConfig
from bow.utils import lowercase, tokenize, build_vocab


class BoWVectorizer:
    """
    Vectorizer chính — điều phối build vocab và vectorize documents.
    """

    def __init__(self):
        self.vocab: dict[str, int] = {}

    def fit(self, documents: list[str], config: BoWConfig) -> "BoWVectorizer":
        """
        Học vocabulary từ danh sách document.
        """
        processed = [lowercase(d) for d in documents] if config.lowercase else documents
        self.vocab = build_vocab(processed)
        self._config = config
        return self

    def transform(self, documents: list[str]) -> list[list[int]]:
        """
        Chuyển danh sách document thành document-term matrix.
        """
        matrix = []
        for doc in documents:
            if self._config.lowercase:
                doc = lowercase(doc)
            tokens = tokenize(doc)
            vector = self._config.strategy.vectorize(tokens, self.vocab)
            matrix.append(vector)
        return matrix

    def fit_transform(self, documents: list[str], config: BoWConfig) -> list[list[int]]:
        """
        Fit và transform trong một bước.
        """
        return self.fit(documents, config).transform(documents)
