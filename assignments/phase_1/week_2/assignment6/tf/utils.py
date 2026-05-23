def lowercase(text: str) -> str:
    return text.lower()


def tokenize(text: str) -> list[str]:
    return text.split()


def count_terms(tokens: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1
    return counts
