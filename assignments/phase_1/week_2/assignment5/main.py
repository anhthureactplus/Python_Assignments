from bow import (
    BoWVectorizer,
    BoWConfig,
    CountBoWStrategy,
    BinaryBoWStrategy,
)

DOCUMENTS = [
    "NLP is fun",
    "I love NLP",
    "NLP NLP NLP",
]


def demo_count():
    print("=" * 60)
    print("DEMO: Count BoW")
    print("=" * 60)

    config = BoWConfig(strategy=CountBoWStrategy(), lowercase=True)
    vectorizer = BoWVectorizer()
    matrix = vectorizer.fit_transform(DOCUMENTS, config)

    print(f"\nVocabulary: {vectorizer.vocab}")
    print(f"\nDocument-Term Matrix:")
    print("[")
    for vec in matrix:
        print(f"  {vec},")
    print("]\n")


def demo_binary():
    print("=" * 60)
    print("BONUS: Binary BoW")
    print("=" * 60)

    config = BoWConfig(strategy=BinaryBoWStrategy(), lowercase=True)
    vectorizer = BoWVectorizer()
    matrix = vectorizer.fit_transform(DOCUMENTS, config)

    print(f"\nVocabulary: {vectorizer.vocab}")
    print(f"\nDocument-Term Matrix:")
    print("[")
    for vec in matrix:
        print(f"  {vec},")
    print("]\n")


if __name__ == "__main__":
    demo_count()
    demo_binary()
