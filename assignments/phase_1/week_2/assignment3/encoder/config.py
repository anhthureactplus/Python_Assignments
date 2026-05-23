"""
config.py — Configuration object cho OneHotEncoder.

OOP Principle: ENCAPSULATION
─────────────────────────────
EncoderConfig gói tất cả tuỳ chọn của encoder vào một object duy nhất.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from encoder.strategies.base import VocabStrategy


class EncoderConfig:
    """
    Đóng gói cấu hình cho một lần chạy encoder.

    Attributes:
        strategy      : chiến lược xây dựng vocabulary (Basic, WithSpecial)
        lowercase     : chuyển text về chữ thường trước khi encode
        add_unk       : thêm token <UNK> cho từ không có trong vocab (Bonus)
        add_pad       : thêm token <PAD> để padding vector (Bonus)
        padding_length: độ dài padding cố định (Bonus)
    """

    def __init__(
        self,
        strategy: "VocabStrategy",
        lowercase: bool = True,
        add_unk: bool = False,
        add_pad: bool = False,
        padding_length: int | None = None,
    ):
        self.strategy = strategy
        self.lowercase = lowercase
        self.add_unk = add_unk
        self.add_pad = add_pad
        self.padding_length = padding_length
