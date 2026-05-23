from assignments.phase_1.week_2.assignment6.tf.tf import (
    TFCalculator,
    TFConfig,
    RawCountTFStrategy,
    NormalizedTFStrategy,
)

DOCUMENT = "NLP NLP is fun"

DOCUMENTS = [
    "NLP is fun",
    "I love NLP",
    "NLP NLP NLP",
]


def demo_normalized():
    print("=" * 60)
    print("DEMO: Normalized TF")
    print("=" * 60)

    config = TFConfig(strategy=NormalizedTFStrategy(), lowercase=True)
    calculator = TFCalculator()
    result = calculator.compute(DOCUMENT, config)

    print(f'\nInput : "{DOCUMENT}"')
    print(f"\nOutput:")
    print("{")
    for term, score in result.items():
        print(f'    "{term}": {score},')
    print("}\n")


def demo_raw():
    print("=" * 60)
    print("BONUS: Raw Count TF")
    print("=" * 60)

    config = TFConfig(strategy=RawCountTFStrategy(), lowercase=True)
    calculator = TFCalculator()
    result = calculator.compute(DOCUMENT, config)

    print(f'\nInput : "{DOCUMENT}"')
    print(f"\nOutput:")
    print("{")
    for term, score in result.items():
        print(f'    "{term}": {score},')
    print("}\n")


def demo_compare():
    print("=" * 60)
    print("BONUS: So sánh Raw vs Normalized TF")
    print("=" * 60)

    raw_config  = TFConfig(strategy=RawCountTFStrategy(),   lowercase=True)
    norm_config = TFConfig(strategy=NormalizedTFStrategy(), lowercase=True)
    calculator  = TFCalculator()

    print(f'\n{"Term":<10} {"Raw Count":>12} {"Normalized":>12}')
    print("-" * 36)

    raw_results  = calculator.compute_batch(DOCUMENTS, raw_config)
    norm_results = calculator.compute_batch(DOCUMENTS, norm_config)

    for i, doc in enumerate(DOCUMENTS):
        print(f'\nDocument: "{doc}"')
        all_terms = raw_results[i].keys()
        for term in all_terms:
            raw  = raw_results[i][term]
            norm = norm_results[i][term]
            print(f"  {term:<10} {raw:>12.1f} {norm:>12.4f}")
    print()


if __name__ == "__main__":
    demo_normalized()
    demo_raw()
    demo_compare()
