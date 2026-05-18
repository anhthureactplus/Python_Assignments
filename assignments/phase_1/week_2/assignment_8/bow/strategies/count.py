from .base import BoWStrategy


class CountBoWStrategy(BoWStrategy):
    """
    Count BoW: đếm số lần xuất hiện của mỗi từ trong document.

    "NLP NLP NLP" → [3, 0, 0, 0, 0]
    """

    def vectorize(self, tokens: list[str], vocab: dict[str, int]) -> list[int]:
        vector = [0] * len(vocab)
        for token in tokens:
            if token in vocab:
                vector[vocab[token]] += 1
        return vector
