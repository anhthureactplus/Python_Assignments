"""OOP search engine: preprocess, vectorize, score, and rank documents."""

from __future__ import annotations

from dataclasses import dataclass

from .config import SearchEngineConfig
from .strategies.base import RankingStrategy
from .utils import cosine_similarity, load_documents, preview, tokenize


@dataclass
class SearchResult:
    rank: int
    path: str
    score: float
    preview: str


class SearchEngine:
    """Mini real-world search engine ranking pipeline."""

    def __init__(self, config: SearchEngineConfig, strategy: RankingStrategy) -> None:
        self.config = config
        self.strategy = strategy
        self.documents: dict[str, str] = {}
        self.tokenized_documents: dict[str, list[str]] = {}
        self.document_vectors: dict[str, dict[str, float]] = {}

    def build_index(self) -> None:
        """Load documents, preprocess them, and build vector index."""
        self.documents = load_documents(self.config)
        self.tokenized_documents = {
            path: tokenize(text, self.config)
            for path, text in self.documents.items()
        }
        self.strategy.fit(self.tokenized_documents)
        self.document_vectors = {
            path: self.strategy.transform_document(tokens)
            for path, tokens in self.tokenized_documents.items()
        }

    def search(self, query: str, top_k: int | None = None) -> list[SearchResult]:
        """Rank documents by cosine similarity to the user query."""
        if not self.document_vectors:
            self.build_index()

        query_tokens = tokenize(query, self.config)
        query_vector = self.strategy.transform_query(query_tokens)

        scored: list[tuple[str, float]] = []
        for path, document_vector in self.document_vectors.items():
            score = cosine_similarity(query_vector, document_vector)
            scored.append((path, score))

        scored.sort(key=lambda item: item[1], reverse=True)
        limit = top_k or self.config.top_k

        return [
            SearchResult(
                rank=index + 1,
                path=path,
                score=score,
                preview=preview(self.documents[path]),
            )
            for index, (path, score) in enumerate(scored[:limit])
        ]
