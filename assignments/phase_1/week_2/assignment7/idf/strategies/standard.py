import math
from .base import IDFStrategy


class StandardIDFStrategy(IDFStrategy):
    """
    Standard IDF: IDF(t) = log(N / df(t))

    Từ xuất hiện ở nhiều document → df lớn → IDF nhỏ (từ phổ biến, ít quan trọng).
    Từ xuất hiện ở ít document   → df nhỏ → IDF lớn (từ hiếm, quan trọng hơn).
    """

    def compute(self, df: dict[str, int], n_docs: int) -> dict[str, float]:
        return {term: math.log(n_docs / count) for term, count in df.items()}
