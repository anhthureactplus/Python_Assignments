from abc import ABC, abstractmethod


class BoWStrategy(ABC):

    @abstractmethod
    def vectorize(self, tokens: list[str], vocab: dict[str, int]) -> list[int]:
        """
        Chuyển danh sách token thành vector BoW theo chiến lược cụ thể.

        Args:
            tokens: danh sách token của một document
            vocab : vocabulary đã build

        Returns:
            list[int] vector có độ dài = len(vocab)
        """
        pass
