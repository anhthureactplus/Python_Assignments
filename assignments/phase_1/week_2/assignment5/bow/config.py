from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bow.strategies.base import BoWStrategy


class BoWConfig:
    """
    Đóng gói cấu hình cho một lần chạy BoW vectorizer.

    Attributes:
        strategy : chiến lược đếm (Count, Binary)
        lowercase: chuyển text về chữ thường
    """

    def __init__(self, strategy: "BoWStrategy", lowercase: bool = True):
        self.strategy = strategy
        self.lowercase = lowercase
