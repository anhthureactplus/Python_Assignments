from .base import TFIDFStrategy
from tfidf.utils import tokenize, compute_tf, compute_df, compute_idf, normalize_vector


class NormalizedTFIDFStrategy(TFIDFStrategy):
    """
    Normalized TF-IDF: smooth TF-IDF + L2 normalization trên mỗi document vector.
    Mỗi vector có độ dài (norm) = 1. (Bonus)
    """

    def compute_matrix(
        self,
        documents: list[str],
        vocab: dict[str, int],
    ) -> list[list[float]]:
        df  = compute_df(documents)
        idf = compute_idf(df, len(documents), smooth=True)

        matrix = []
        for doc in documents:
            tokens = tokenize(doc)
            tf     = compute_tf(tokens)
            vector = [tf.get(term, 0.0) * idf.get(term, 0.0) for term in vocab]
            matrix.append(normalize_vector(vector))
        return matrix
