import math


def lowercase(text: str) -> str:
    return text.lower()


def tokenize(text: str) -> list[str]:
    return text.split()


def build_vocab(documents: list[str]) -> dict[str, int]:
    vocab: dict[str, int] = {}
    for doc in documents:
        for token in tokenize(doc):
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab


def compute_tf(tokens: list[str]) -> dict[str, float]:
    total = len(tokens)
    counts: dict[str, int] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1
    return {term: count / total for term, count in counts.items()}


def compute_df(documents: list[str]) -> dict[str, int]:
    df: dict[str, int] = {}
    for doc in documents:
        for token in set(tokenize(doc)):
            df[token] = df.get(token, 0) + 1
    return df


def compute_idf(df: dict[str, int], n_docs: int, smooth: bool = False) -> dict[str, float]:
    if smooth:
        return {term: math.log(n_docs / (count + 1)) + 1 for term, count in df.items()}
    return {term: math.log(n_docs / count) for term, count in df.items()}


def normalize_vector(vector: list[float]) -> list[float]:
    norm = math.sqrt(sum(v ** 2 for v in vector))
    if norm == 0:
        return vector
    return [v / norm for v in vector]
