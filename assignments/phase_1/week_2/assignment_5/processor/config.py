"""
config.py — Configuration object cho VietnameseTextProcessor.

OOP Principle: ENCAPSULATION
─────────────────────────────
ProcessorConfig gói tất cả tuỳ chọn của pipeline vào một object duy nhất.
Thay vì truyền nhiều tham số rời rạc đi khắp nơi, ta chỉ truyền một config.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from processor.strategies.base import CleanStrategy


class ProcessorConfig:
    """
    Đóng gói cấu hình cho một lần chạy pipeline.

    Attributes:
        clean_strategy  : chiến lược làm sạch văn bản (Basic, Aggressive, ...)
        lowercase       : chuyển về chữ thường
        remove_stopwords: bật/tắt loại stopword
        stopwords_path  : đường dẫn file .txt chứa stopword (Bonus)
    """

    def __init__(
        self,
        clean_strategy: "CleanStrategy",
        lowercase: bool = True,
        remove_stopwords: bool = False,
        stopwords_path: str | None = None,
    ):
        self.clean_strategy = clean_strategy
        self.lowercase = lowercase
        self.remove_stopwords = remove_stopwords
        self.stopwords_path = stopwords_path
