import math
from .base import IDFStrategy


class SmoothIDFStrategy(IDFStrategy):
    """
    Smooth IDF: IDF(t) = log(N / (df(t) + 1)) + 1

    Thêm +1 vào mẫu số để tránh chia cho 0 khi df(t) = N.
    Thêm +1 bên ngoài để IDF không bao giờ = 0.
    Thường được dùng trong scikit-learn TfidfVectorizer.
    """

    def compute(self, df: dict[str, int], n_docs: int) -> dict[str, float]:
        return {term: math.log(n_docs / (count + 1)) + 1 for term, count in df.items()}
