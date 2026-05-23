from tfidf import (
    TFIDFVectorizer,
    TFIDFConfig,
    StandardTFIDFStrategy,
    SmoothTFIDFStrategy,
    NormalizedTFIDFStrategy,
)

DOCUMENTS = [
    "I love NLP",
    "NLP is fun",
    "I love machine learning",
]


def print_matrix(matrix: list[list[float]], vocab: dict[str, int], documents: list[str]):
    terms = list(vocab.keys())
    col_w = 10

    header = f"{'':20}" + "".join(f"{t:>{col_w}}" for t in terms)
    print(header)
    print("-" * len(header))
    for doc, row in zip(documents, matrix):
        label = f'"{doc}"'[:19]
        vals  = "".join(f"{v:>{col_w}.4f}" for v in row)
        print(f"{label:<20}{vals}")
    print()


def demo_standard():
    print("=" * 60)
    print("DEMO: Standard TF-IDF")
    print("=" * 60)

    config     = TFIDFConfig(strategy=StandardTFIDFStrategy(), lowercase=True)
    vectorizer = TFIDFVectorizer()
    matrix     = vectorizer.fit_transform(DOCUMENTS, config)

    print(f"\nVocabulary: {vectorizer.vocab}\n")
    print_matrix(matrix, vectorizer.vocab, DOCUMENTS)


def demo_smooth():
    print("=" * 60)
    print("BONUS: Smooth TF-IDF")
    print("=" * 60)

    config     = TFIDFConfig(strategy=SmoothTFIDFStrategy(), lowercase=True)
    vectorizer = TFIDFVectorizer()
    matrix     = vectorizer.fit_transform(DOCUMENTS, config)

    print()
    print_matrix(matrix, vectorizer.vocab, DOCUMENTS)


def demo_normalized():
    print("=" * 60)
    print("BONUS: Normalized TF-IDF (L2)")
    print("=" * 60)

    config     = TFIDFConfig(strategy=NormalizedTFIDFStrategy(), lowercase=True)
    vectorizer = TFIDFVectorizer()
    matrix     = vectorizer.fit_transform(DOCUMENTS, config)

    print()
    print_matrix(matrix, vectorizer.vocab, DOCUMENTS)


if __name__ == "__main__":
    demo_standard()
    demo_smooth()
    demo_normalized()
