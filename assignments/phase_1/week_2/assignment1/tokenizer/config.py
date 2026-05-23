"""
config.py — Configuration object cho WhitespaceTokenizer.

OOP Principle: ENCAPSULATION
─────────────────────────────
TokenizerConfig gói (encapsulate) tất cả các tuỳ chọn xử lý văn bản
vào một đơn vị duy nhất. Thay vì truyền nhiều tham số rời rạc đi khắp nơi,
ta truyền một config object — dữ liệu đi cùng nhau, dễ quản lý, dễ mở rộng.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tokenizer.strategies.base import TokenizeStrategy


class TokenizerConfig:
    """
    Đóng gói cấu hình cho một lần chạy tokenizer.

    Attributes:
        strategy: chiến lược xử lý token (Basic, RemovePunctuation, ...)
        lowercase: chuyển text về chữ thường trước khi tokenize
        count_frequency: có đếm tần suất token hay không
    """

    def __init__(
        self,
        strategy: "TokenizeStrategy",
        lowercase: bool = True,
        count_frequency: bool = False,
    ):
        self.strategy = strategy
        self.lowercase = lowercase
        self.count_frequency = count_frequency