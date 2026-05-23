from idf.config import IDFConfig
from idf.utils import lowercase, tokenize, compute_document_frequency


class IDFCalculator:
    """
    Calculator chính — điều phối tính document frequency và IDF.
    """

    def compute(self, documents: list[str], config: IDFConfig) -> dict[str, float]:
        """
        Tính IDF cho toàn bộ corpus.

        Args:
            documents: danh sách document
            config   : cấu hình IDF

        Returns:
            dict ánh xạ token → IDF score
        """
        if config.lowercase:
            documents = [lowercase(d) for d in documents]

        df = compute_document_frequency(documents)
        n_docs = len(documents)

        return config.strategy.compute(df, n_docs)

    def document_frequency(self, documents: list[str], config: IDFConfig) -> dict[str, int]:
        """
        Trả về document frequency của mỗi từ trong corpus.
        """
        if config.lowercase:
            documents = [lowercase(d) for d in documents]
        return compute_document_frequency(documents)
