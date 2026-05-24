"""Configuration object for the mini search engine."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class SearchEngineConfig:
    """Store all settings needed for ranking documents."""

    data_dir: str | Path = "data"
    top_k: int = 5
    lowercase: bool = True
    remove_stopwords: bool = True
    min_token_length: int = 2
    allowed_extensions: tuple[str, ...] = (".txt", ".md", ".html")

    def __post_init__(self) -> None:
        self.data_dir = Path(self.data_dir)

    def accepts_file(self, path: Path) -> bool:
        """Return True if the file extension is allowed."""
        return path.suffix.lower() in self.allowed_extensions

    @classmethod
    def from_extensions(cls, extensions: Iterable[str], **kwargs) -> "SearchEngineConfig":
        normalized = tuple(ext if ext.startswith(".") else f".{ext}" for ext in extensions)
        return cls(allowed_extensions=normalized, **kwargs)
