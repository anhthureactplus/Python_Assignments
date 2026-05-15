"""
utils.py — Helper functions chung cho toàn package.

Module này KHÔNG chứa class OOP nào — chỉ là pure functions.
Việc tách helper ra module riêng giúp:
  - Tái sử dụng giữa các strategy khác nhau
  - Dễ test độc lập từng hàm
  - Tránh ô nhiễm namespace của các module chính
"""

import re


def lowercase(text: str) -> str:
    """
    Chuyển toàn bộ text về chữ thường.

    Example:
        >>> lowercase("Hello NLP")
        'hello nlp'
    """
    return text.lower()


def remove_urls(text: str) -> str:
    """
    Xoá tất cả URL (http, https, www) ra khỏi text.

    Example:
        >>> remove_urls("Visit https://abc.com now")
        'Visit  now'
    """
    return re.sub(r"https?://\S+|www\.\S+", "", text)


def remove_html(text: str) -> str:
    """
    Xoá tất cả thẻ HTML ra khỏi text.

    Example:
        >>> remove_html("<p>Hello</p>")
        'Hello'
    """
    return re.sub(r"<[^>]+>", "", text)


def remove_emojis(text: str) -> str:
    """
    Xoá tất cả emoji ra khỏi text bằng Unicode range.

    Example:
        >>> remove_emojis("I love NLP 😄🔥")
        'I love NLP '
    """
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002500-\U00002BEF"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001F926-\U0001F937"
        "\U00010000-\U0010FFFF"
        "\u2640-\u2642"
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\ufe0f"
        "\u3030"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub("", text)


def remove_punctuation(text: str) -> str:
    """
    Xoá dấu câu ra khỏi text, giữ lại chữ cái (kể cả tiếng Việt) và số.

    Example:
        >>> remove_punctuation("Hello, world!!!")
        'Hello world'
    """
    return re.sub(r"[^\w\s]", "", text)


def normalize_whitespace(text: str) -> str:
    """
    Gộp nhiều khoảng trắng/tab/newline thành một dấu cách, strip hai đầu.

    Example:
        >>> normalize_whitespace("hello    world\\n\\nfoo")
        'hello world foo'
    """
    return re.sub(r"\s+", " ", text).strip()


def load_stopwords(path: str) -> set[str]:
    """
    Đọc danh sách stopword từ file .txt (mỗi từ một dòng).

    Args:
        path: đường dẫn đến file stopwords .txt

    Returns:
        set các stopword (lowercase)

    Bonus: hỗ trợ load stopwords từ file ngoài.
    """
    with open(path, encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}


def filter_stopwords(tokens: list[str], stopwords: set[str]) -> list[str]:
    """
    Lọc bỏ các token nằm trong tập stopwords.

    Args:
        tokens   : danh sách token
        stopwords: tập từ cần loại bỏ

    Returns:
        danh sách token đã lọc
    """
    return [t for t in tokens if t.lower() not in stopwords]
