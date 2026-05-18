def lowercase(text: str) -> str:
    return text.lower()


def tokenize(text: str) -> list[str]:
    return text.split()


def build_vocab(documents: list[str]) -> dict[str, int]:
    """
    Xây dựng vocabulary từ danh sách document, sắp xếp theo thứ tự xuất hiện.
    """
    vocab: dict[str, int] = {}
    for doc in documents:
        for token in tokenize(doc):
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab
