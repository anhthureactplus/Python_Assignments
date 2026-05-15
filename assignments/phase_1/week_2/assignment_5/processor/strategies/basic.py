"""
strategies/basic.py — Chiến lược làm sạch cơ bản.

OOP Principles:
  - INHERITANCE : kế thừa từ CleanStrategy, tái sử dụng interface chung
  - POLYMORPHISM: cùng method `clean` nhưng chỉ xoá HTML + normalize space
"""

from .base import CleanStrategy
from processor.utils import remove_html, normalize_whitespace


class BasicCleanStrategy(CleanStrategy):
    """
    Chiến lược làm sạch tối thiểu: chỉ xoá thẻ HTML và chuẩn hoá khoảng trắng.

    Giữ nguyên URL, emoji, dấu câu.
    Phù hợp khi chỉ cần bóc tách HTML đơn giản.
    """

    def clean(self, text: str) -> str:
        """
        Xoá HTML → normalize whitespace.

        Example:
            >>> BasicCleanStrategy().clean("<p>Hello  world!</p>")
            'Hello world!'
        """
        text = remove_html(text)
        text = normalize_whitespace(text)
        return text
