"""Bonus strategy: raw word counts."""

from __future__ import annotations

from collections import Counter

from .base import RankingStrategy


class RawCountStrategy(RankingStrategy):
    """Vectorize text by absolute word count."""

    def fit(self, tokenized_documents: dict[str, list[str]]) -> None:
        return None

    def transform_document(self, tokens: list[str]) -> dict[str, float]:
        return dict(Counter(tokens))

    def transform_query(self, tokens: list[str]) -> dict[str, float]:
        return dict(Counter(tokens))
