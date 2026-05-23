from .base import TFStrategy
from tf.utils import count_terms


class RawCountTFStrategy(TFStrategy):
    """
    Raw Count TF: số lần xuất hiện tuyệt đối của từ trong document.

    "NLP NLP is fun" → {'nlp': 2, 'is': 1, 'fun': 1}
    """

    def compute(self, tokens: list[str]) -> dict[str, float]:
        return {term: float(count) for term, count in count_terms(tokens).items()}
