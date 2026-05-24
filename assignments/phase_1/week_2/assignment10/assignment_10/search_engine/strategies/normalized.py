"""Alternative strategy: normalized term frequency only."""

from __future__ import annotations

from collections import Counter

from .base import RankingStrategy


class NormalizedTfStrategy(RankingStrategy):
    """Vectorize by count(term) / total words."""

    def fit(self, tokenized_documents: dict[str, list[str]]) -> None:
        return None

    def _normalized_counts(self, tokens: list[str]) -> dict[str, float]:
        if not tokens:
            return {}
        counts = Counter(tokens)
        total = len(tokens)
        return {term: count / total for term, count in counts.items()}

    def transform_document(self, tokens: list[str]) -> dict[str, float]:
        return self._normalized_counts(tokens)

    def transform_query(self, tokens: list[str]) -> dict[str, float]:
        return self._normalized_counts(tokens)
