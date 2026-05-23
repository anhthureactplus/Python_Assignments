from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from idf.strategies.base import IDFStrategy


class IDFConfig:
    """
    Đóng gói cấu hình cho một lần chạy IDF calculator.

    Attributes:
        strategy : chiến lược tính IDF (Standard, Smooth)
        lowercase: chuyển text về chữ thường
    """

    def __init__(self, strategy: "IDFStrategy", lowercase: bool = True):
        self.strategy = strategy
        self.lowercase = lowercase
