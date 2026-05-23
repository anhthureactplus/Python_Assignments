from .base import TFIDFStrategy
from tfidf.utils import tokenize, compute_tf, compute_df, compute_idf


class SmoothTFIDFStrategy(TFIDFStrategy):
    """
    Smooth TF-IDF: dùng smooth IDF = log(N / (df+1)) + 1
    Tránh chia cho 0, IDF không bao giờ = 0. (Bonus)
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
            matrix.append(vector)
        return matrix
