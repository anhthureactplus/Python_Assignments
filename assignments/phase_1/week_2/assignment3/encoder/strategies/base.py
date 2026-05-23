"""
strategies/base.py — Abstract base class cho mọi vocab strategy.

OOP Principle: ABSTRACTION
─────────────────────────────
VocabStrategy định nghĩa hợp đồng mà mọi chiến lược xây dựng vocab phải tuân thủ.
Buộc subclass implement `build_vocab()`, không thể khởi tạo trực tiếp.
"""

from abc import ABC, abstractmethod


class VocabStrategy(ABC):
    """
    Interface cho các chiến lược xây dựng vocabulary.

    Mọi subclass phải implement method `build_vocab()`.
    """

    @abstractmethod
    def build_vocab(self, sentences: list[str]) -> dict[str, int]:
        """
        Xây dựng vocabulary từ danh sách câu.

        Args:
            sentences: danh sách câu đầu vào

        Returns:
            dict ánh xạ token → index
        """
        pass
