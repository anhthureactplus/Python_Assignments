"""Abstract base strategy for document vectorization."""

from __future__ import annotations

from abc import ABC, abstractmethod


class RankingStrategy(ABC):
    """Interface for all ranking/vectorization strategies."""

    @abstractmethod
    def fit(self, tokenized_documents: dict[str, list[str]]) -> None:
        """Learn statistics from the document corpus."""
        raise NotImplementedError

    @abstractmethod
    def transform_document(self, tokens: list[str]) -> dict[str, float]:
        """Convert one document into a vector."""
        raise NotImplementedError

    @abstractmethod
    def transform_query(self, tokens: list[str]) -> dict[str, float]:
        """Convert one user query into a vector."""
        raise NotImplementedError
