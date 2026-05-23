from .base import BoWStrategy


class BinaryBoWStrategy(BoWStrategy):
    """
    Binary BoW: 1 nếu từ xuất hiện, 0 nếu không — bất kể số lần.

    "NLP NLP NLP" → [1, 0, 0, 0, 0]
    """

    def vectorize(self, tokens: list[str], vocab: dict[str, int]) -> list[int]:
        vector = [0] * len(vocab)
        for token in tokens:
            if token in vocab:
                vector[vocab[token]] = 1
        return vector
