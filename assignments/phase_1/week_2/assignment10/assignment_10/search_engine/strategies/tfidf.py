"""Main required strategy: TF-IDF vectorization."""

from __future__ import annotations

import math
from collections import Counter

from .base import RankingStrategy


class TfidfStrategy(RankingStrategy):
    """Compute TF-IDF vectors for documents and queries.

    TF is normalized term frequency: count(term) / total terms.
    IDF is smoothed: log((N + 1) / (df + 1)) + 1.
    """

    def __init__(self) -> None:
        self.idf: dict[str, float] = {}
        self.vocabulary: set[str] = set()

    def fit(self, tokenized_documents: dict[str, list[str]]) -> None:
        total_documents = len(tokenized_documents)
        document_frequency: Counter[str] = Counter()

        for tokens in tokenized_documents.values():
            unique_terms = set(tokens)
            document_frequency.update(unique_terms)
            self.vocabulary.update(unique_terms)

        self.idf = {
            term: math.log((total_documents + 1) / (df + 1)) + 1
            for term, df in document_frequency.items()
        }

    def _term_frequency(self, tokens: list[str]) -> dict[str, float]:
        if not tokens:
            return {}
        counts = Counter(tokens)
        total = len(tokens)
        return {term: count / total for term, count in counts.items()}

    def _tfidf(self, tokens: list[str]) -> dict[str, float]:
        tf = self._term_frequency(tokens)
        return {
            term: freq * self.idf.get(term, 0.0)
            for term, freq in tf.items()
            if term in self.vocabulary
        }

    def transform_document(self, tokens: list[str]) -> dict[str, float]:
        return self._tfidf(tokens)

    def transform_query(self, tokens: list[str]) -> dict[str, float]:
        return self._tfidf(tokens)
