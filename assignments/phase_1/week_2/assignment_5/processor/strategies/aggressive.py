"""
strategies/aggressive.py — Chiến lược làm sạch toàn diện.

OOP Principles:
  - INHERITANCE : kế thừa từ CleanStrategy, tái sử dụng interface chung
  - POLYMORPHISM: cùng method `clean` nhưng xoá HTML + URL + emoji + dấu câu
  - ENCAPSULATION: toàn bộ pipeline làm sạch được đóng gói bên trong strategy
"""

from .base import CleanStrategy
from processor.utils import (
    remove_html,
    remove_urls,
    remove_emojis,
    remove_punctuation,
    normalize_whitespace,
)


class AggressiveCleanStrategy(CleanStrategy):
    """
    Chiến lược làm sạch toàn diện: xoá HTML, URL, emoji, dấu câu.

    Token sau khi xử lý chỉ còn chữ cái và số.
    Phù hợp cho các tác vụ NLP cần văn bản sạch nhất có thể.
    """

    def clean(self, text: str) -> str:
        """
        Xoá HTML → URL → emoji → dấu câu → normalize whitespace.

        Example:
            >>> AggressiveCleanStrategy().clean("<p>Hello 😄</p> https://x.com now!!!")
            'Hello now'
        """
        text = remove_html(text)
        text = remove_urls(text)
        text = remove_emojis(text)
        text = remove_punctuation(text)
        text = normalize_whitespace(text)
        return text
