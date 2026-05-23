def lowercase(text: str) -> str:
    return text.lower()


def tokenize(text: str) -> list[str]:
    return text.split()


def compute_document_frequency(documents: list[str]) -> dict[str, int]:
    """
    Đếm số document chứa mỗi từ (df).

    Mỗi document chỉ được đếm một lần dù từ xuất hiện nhiều lần.
    """
    df: dict[str, int] = {}
    for doc in documents:
        seen = set(tokenize(doc))
        for token in seen:
            df[token] = df.get(token, 0) + 1
    return df
