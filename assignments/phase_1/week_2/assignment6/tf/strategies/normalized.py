from .base import TFStrategy
from tf.utils import count_terms


class NormalizedTFStrategy(TFStrategy):
    """
    Normalized TF: TF(t,d) = count(t) / total_terms(d)

    "NLP NLP is fun" → {'nlp': 0.5, 'is': 0.25, 'fun': 0.25}
    """

    def compute(self, tokens: list[str]) -> dict[str, float]:
        total = len(tokens)
        counts = count_terms(tokens)
        return {term: count / total for term, count in counts.items()}
