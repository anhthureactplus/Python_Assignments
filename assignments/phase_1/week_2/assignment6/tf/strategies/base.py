from abc import ABC, abstractmethod


class TFStrategy(ABC):

    @abstractmethod
    def compute(self, tokens: list[str]) -> dict[str, float]:
        """
        Tính TF cho danh sách token của một document.

        Args:
            tokens: danh sách token

        Returns:
            dict ánh xạ token → TF score
        """
        pass
