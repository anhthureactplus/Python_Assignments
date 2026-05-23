from .base import TFIDFStrategy
from tfidf.utils import tokenize, compute_tf, compute_df, compute_idf


class StandardTFIDFStrategy(TFIDFStrategy):
    """
    Standard TF-IDF: TF(t,d) × IDF(t) = (count/total) × log(N/df)
    """

    def compute_matrix(
        self,
        documents: list[str],
        vocab: dict[str, int],
    ) -> list[list[float]]:
        df  = compute_df(documents)
        idf = compute_idf(df, len(documents), smooth=False)

        matrix = []
        for doc in documents:
            tokens = tokenize(doc)
            tf     = compute_tf(tokens)
            vector = [tf.get(term, 0.0) * idf.get(term, 0.0) for term in vocab]
            matrix.append(vector)
        return matrix
