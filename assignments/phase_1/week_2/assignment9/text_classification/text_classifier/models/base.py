from abc import ABC, abstractmethod


class BaseClassifier(ABC):
    """Abstract base class for classifiers."""

    @abstractmethod
    def fit(self, X_train, y_train):
        pass

    @abstractmethod
    def predict(self, X_test):
        pass

    @abstractmethod
    def name(self) -> str:
        pass
