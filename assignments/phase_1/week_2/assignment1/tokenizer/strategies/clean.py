"""
strategies/clean.py — Chiến lược tokenize nâng cao: xoá dấu câu trước khi tách.

OOP Principles:
  - INHERITANCE: kế thừa từ TokenizeStrategy, tái sử dụng interface chung
  - POLYMORPHISM: cùng method `tokenize` nhưng XOÁ dấu câu trước khi split
  - ENCAPSULATION: bước xoá dấu câu được đóng gói bên trong strategy,
    người gọi không cần biết chi tiết bên trong
"""

from .base import TokenizeStrategy
from tokenizer.utils import remove_punctuation


class CleanTokenizeStrategy(TokenizeStrategy):
    """
    Chiến lược tokenize sạch: loại bỏ dấu câu trước khi split.

    Token sau khi xử lý không còn dấu câu (ví dụ: "world!" → "world").
    Phù hợp cho các tác vụ NLP cần token thuần chữ cái/số.
    """

    def tokenize(self, text: str) -> list[str]:
        """
        Xoá dấu câu rồi tách bằng split().

        Example:
            >>> CleanTokenizeStrategy().tokenize("hello, world!")
            ['hello', 'world']
        """
        clean_text = remove_punctuation(text)
        return clean_text.split()