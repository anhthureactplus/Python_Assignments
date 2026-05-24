"""Utility functions: load files, preprocess text, and vector math."""

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Iterable

from .config import SearchEngineConfig

STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "is", "are", "was", "were",
    "be", "been", "being", "to", "of", "in", "on", "for", "with", "as", "by", "at",
    "from", "this", "that", "these", "those", "it", "its", "into", "about", "can", "will",
    "your", "you", "we", "our", "they", "their", "he", "she", "his", "her", "them",
}

TOKEN_PATTERN = re.compile(r"[a-zA-Z0-9]+")
TAG_PATTERN = re.compile(r"<[^>]+>")


def strip_html(text: str) -> str:
    """Remove simple HTML tags from crawled pages."""
    return TAG_PATTERN.sub(" ", text)


def tokenize(text: str, config: SearchEngineConfig) -> list[str]:
    """Convert raw document text into clean tokens."""
    text = strip_html(text)
    if config.lowercase:
        text = text.lower()

    tokens = TOKEN_PATTERN.findall(text)
    tokens = [token for token in tokens if len(token) >= config.min_token_length]

    if config.remove_stopwords:
        tokens = [token for token in tokens if token not in STOP_WORDS]

    return tokens


def load_documents(config: SearchEngineConfig) -> dict[str, str]:
    """Load all accepted documents from data_dir recursively."""
    documents: dict[str, str] = {}

    if not config.data_dir.exists():
        raise FileNotFoundError(
            f"Data folder not found: {config.data_dir}. Create it and add crawled files."
        )

    for path in sorted(config.data_dir.rglob("*")):
        if path.is_file() and config.accepts_file(path):
            try:
                documents[str(path)] = path.read_text(encoding="utf-8", errors="ignore")
            except OSError as exc:
                print(f"Skipping {path}: {exc}")

    if not documents:
        raise ValueError(f"No valid documents found in {config.data_dir}")

    return documents


def dot_product(a: dict[str, float], b: dict[str, float]) -> float:
    """Compute dot product between sparse vectors."""
    if len(a) > len(b):
        a, b = b, a
    return sum(value * b.get(term, 0.0) for term, value in a.items())


def magnitude(vector: dict[str, float]) -> float:
    """Compute vector length."""
    return math.sqrt(sum(value * value for value in vector.values()))


def cosine_similarity(a: dict[str, float], b: dict[str, float]) -> float:
    """Compute cosine similarity between two sparse vectors."""
    denominator = magnitude(a) * magnitude(b)
    if denominator == 0:
        return 0.0
    return dot_product(a, b) / denominator


def preview(text: str, max_chars: int = 140) -> str:
    """Return a short one-line preview for CLI output."""
    compact = " ".join(strip_html(text).split())
    return compact[:max_chars] + ("..." if len(compact) > max_chars else "")
