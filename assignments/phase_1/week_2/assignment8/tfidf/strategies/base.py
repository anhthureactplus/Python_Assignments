from abc import ABC, abstractmethod


class TFIDFStrategy(ABC):

    @abstractmethod
    def compute_matrix(
        self,
        documents: list[str],
        vocab: dict[str, int],
    ) -> list[list[float]]:
        """
        Tính TF-IDF matrix cho toàn bộ corpus.

        Args:
            documents: danh sách document đã lowercase
            vocab    : vocabulary đã build

        Returns:
            matrix shape (n_docs, vocab_size)
        """
        pass
