from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tfidf.strategies.base import TFIDFStrategy


class TFIDFConfig:
    """
    Đóng gói cấu hình cho một lần chạy TF-IDF vectorizer.

    Attributes:
        strategy : chiến lược tính TF-IDF (Standard, Smooth, Normalized)
        lowercase: chuyển text về chữ thường
    """

    def __init__(self, strategy: "TFIDFStrategy", lowercase: bool = True):
        self.strategy = strategy
        self.lowercase = lowercase
