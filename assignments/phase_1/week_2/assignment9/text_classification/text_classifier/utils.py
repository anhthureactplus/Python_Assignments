import re
from typing import Iterable, List


def preprocess_text(text: str) -> str:
    """Lowercase, remove URLs, punctuation-like symbols, and extra spaces."""
    if text is None:
        return ""

    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-ZÀ-ỹ\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_texts(texts: Iterable[str]) -> List[str]:
    return [preprocess_text(text) for text in texts]
