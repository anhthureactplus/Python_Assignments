from idf import (
    IDFCalculator,
    IDFConfig,
    StandardIDFStrategy,
    SmoothIDFStrategy,
)

DOCUMENTS = [
    "NLP is fun",
    "I love NLP",
    "NLP NLP NLP",
    "Deep learning is powerful",
]


def demo_standard():
    print("=" * 60)
    print("DEMO: Standard IDF  —  log(N / df(t))")
    print("=" * 60)

    config = IDFConfig(strategy=StandardIDFStrategy(), lowercase=True)
    calculator = IDFCalculator()

    df     = calculator.document_frequency(DOCUMENTS, config)
    scores = calculator.compute(DOCUMENTS, config)

    print(f"\nN = {len(DOCUMENTS)} documents\n")
    print(f"{'Term':<12} {'df':>6} {'IDF':>10}")
    print("-" * 32)
    for term, score in sorted(scores.items(), key=lambda x: -x[1]):
        print(f"  {term:<12} {df[term]:>6} {score:>10.4f}")
    print()


def demo_smooth():
    print("=" * 60)
    print("BONUS: Smooth IDF  —  log(N / (df(t)+1)) + 1")
    print("=" * 60)

    config = IDFConfig(strategy=SmoothIDFStrategy(), lowercase=True)
    calculator = IDFCalculator()
    scores = calculator.compute(DOCUMENTS, config)

    print(f"\n{'Term':<12} {'IDF (smooth)':>14}")
    print("-" * 28)
    for term, score in sorted(scores.items(), key=lambda x: -x[1]):
        print(f"  {term:<12} {score:>14.4f}")
    print()


def demo_explain():
    print("=" * 60)
    print("BONUS: Tại sao từ phổ biến có IDF thấp?")
    print("=" * 60)

    config = IDFConfig(strategy=StandardIDFStrategy(), lowercase=True)
    calculator = IDFCalculator()
    df     = calculator.document_frequency(DOCUMENTS, config)
    scores = calculator.compute(DOCUMENTS, config)
    n      = len(DOCUMENTS)

    print(f"\n  'nlp'  xuất hiện trong {df['nlp']}/{n} docs → IDF = {scores['nlp']:.4f}  (thấp — phổ biến)")
    print(f"  'love' xuất hiện trong {df['love']}/{n} docs → IDF = {scores['love']:.4f}  (cao  — hiếm)\n")
    print("  → Từ nào xuất hiện càng nhiều document, IDF càng nhỏ,")
    print("    đóng góp ít hơn vào TF-IDF score cuối cùng.\n")


if __name__ == "__main__":
    demo_standard()
    demo_smooth()
    demo_explain()
