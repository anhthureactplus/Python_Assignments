from abc import ABC, abstractmethod


class IDFStrategy(ABC):

    @abstractmethod
    def compute(self, df: dict[str, int], n_docs: int) -> dict[str, float]:
        """
        Tính IDF cho toàn bộ vocabulary.

        Args:
            df    : document frequency của mỗi từ
            n_docs: tổng số document

        Returns:
            dict ánh xạ token → IDF score
        """
        pass
