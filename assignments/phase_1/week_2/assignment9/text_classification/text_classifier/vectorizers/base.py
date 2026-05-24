from abc import ABC, abstractmethod


class BaseVectorizer(ABC):
    """Abstract base class for text vectorizers."""

    @abstractmethod
    def fit_transform(self, texts):
        pass

    @abstractmethod
    def transform(self, texts):
        pass

    @abstractmethod
    def name(self) -> str:
        pass
