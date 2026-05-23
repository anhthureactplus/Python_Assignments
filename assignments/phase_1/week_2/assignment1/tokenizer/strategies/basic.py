"""
strategies/basic.py — Chiến lược tokenize cơ bản: tách bằng khoảng trắng.

OOP Principles:
  - INHERITANCE: kế thừa từ TokenizeStrategy, tái sử dụng interface chung
  - POLYMORPHISM: cùng method `tokenize` nhưng KHÔNG xoá dấu câu
"""

from .base import TokenizeStrategy


class BasicTokenizeStrategy(TokenizeStrategy):
    """
    Chiến lược tokenize đơn giản: split() theo whitespace.

    Token giữ nguyên dấu câu (ví dụ: "world!" → "world!").
    Phù hợp khi cần giữ nguyên hình thức từ gốc.
    """

    def tokenize(self, text: str) -> list[str]:
        """
        Tách văn bản bằng str.split() — tự động bỏ khoảng trắng thừa.

        Example:
            >>> BasicTokenizeStrategy().tokenize("hello world!")
            ['hello', 'world!']
        """
        return text.split()