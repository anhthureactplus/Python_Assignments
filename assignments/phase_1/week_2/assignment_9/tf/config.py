from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tf.strategies.base import TFStrategy


class TFConfig:
    """
    Đóng gói cấu hình cho một lần chạy TF calculator.

    Attributes:
        strategy : chiến lược tính TF (RawCount, Normalized)
        lowercase: chuyển text về chữ thường
    """

    def __init__(self, strategy: "TFStrategy", lowercase: bool = True):
        self.strategy = strategy
        self.lowercase = lowercase
