"""
strategies/base.py — Abstract base class cho mọi tokenize strategy.

OOP Principle: ABSTRACTION
─────────────────────────────
TokenizeStrategy là một abstract base class (ABC) định nghĩa hợp đồng
(contract) mà mọi chiến lược tokenize phải tuân thủ. Nó KHÔNG implement
chi tiết — chỉ phơi ra interface "cái gì cần làm".

Decorator @abstractmethod buộc subclass phải override method `tokenize()`,
và bản thân TokenizeStrategy không thể được khởi tạo trực tiếp.
"""

from abc import ABC, abstractmethod


class TokenizeStrategy(ABC):
    """
    Interface cho các chiến lược tokenize.

    Mọi subclass phải implement method `tokenize()` với chữ ký này.
    """

    @abstractmethod
    def tokenize(self, text: str) -> list[str]:
        """
        Tách văn bản thành danh sách token.

        Args:
            text: chuỗi đã được normalize (lowercase + whitespace)

        Returns:
            list[str] các token
        """
        pass