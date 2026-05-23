"""
utils.py — Helper functions chung cho toàn package.

Module này KHÔNG chứa class OOP nào — chỉ là pure functions.
Việc tách helper ra module riêng giúp:
  - Tái sử dụng giữa các strategy khác nhau
  - Dễ test độc lập
  - Tránh ô nhiễm namespace của các module chính
"""

import re


def lowercase(text: str) -> str:
    """
    Chuyển toàn bộ text về chữ thường.

    Args:
        text: chuỗi văn bản đầu vào

    Returns:
        chuỗi đã lowercase

    Example:
        >>> lowercase("Hello World")
        'hello world'
    """
    return text.lower()


def normalize_whitespace(text: str) -> str:
    """
    Chuẩn hoá khoảng trắng: gộp nhiều space/tab/newline thành một dấu cách.

    Args:
        text: chuỗi văn bản đầu vào

    Returns:
        chuỗi đã chuẩn hoá, strip() hai đầu

    Example:
        >>> normalize_whitespace("hello    world\\n\\nfoo")
        'hello world foo'
    """
    return re.sub(r"\s+", " ", text).strip()


def remove_punctuation(text: str) -> str:
    """
    Loại bỏ các ký tự dấu câu ra khỏi text.

    Args:
        text: chuỗi văn bản đầu vào

    Returns:
        chuỗi đã xoá dấu câu

    Example:
        >>> remove_punctuation("hello, world!")
        'hello world'
    """
    return re.sub(r"[^\w\s]", "", text)


def count_frequency(tokens: list[str]) -> dict[str, int]:
    """
    Đếm tần suất xuất hiện của từng token.

    Args:
        tokens: danh sách token

    Returns:
        dict ánh xạ token → số lần xuất hiện, sắp xếp giảm dần

    Example:
        >>> count_frequency(["a", "b", "a"])
        {'a': 2, 'b': 1}
    """
    freq: dict[str, int] = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))