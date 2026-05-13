"""
main.py — Demo cách sử dụng package tokenizer.

File này minh hoạ POLYMORPHISM trong thực tế: cùng một WhitespaceTokenizer,
chỉ cần đổi strategy trong config là có hành vi tokenize khác nhau,
KHÔNG cần sửa bất kỳ dòng nào trong WhitespaceTokenizer.run().
"""

from tokenizer import (
    WhitespaceTokenizer,
    TokenizerConfig,
    BasicTokenizeStrategy,
    CleanTokenizeStrategy,
)

SAMPLE_TEXT = """Hello world!   
NLP is fun.
"""

BATCH_TEXTS = [
    "I love NLP",
    "Tokenization is easy",
]


def demo_basic():
    """Demo tokenize cơ bản — giữ nguyên dấu câu."""
    print("=" * 60)
    print("DEMO: Basic Tokenize (giữ dấu câu)")
    print("=" * 60)

    config = TokenizerConfig(
        strategy=BasicTokenizeStrategy(),
        lowercase=True,
        count_frequency=False,
    )

    tokenizer = WhitespaceTokenizer()
    tokens = tokenizer.run(SAMPLE_TEXT, config)
    print(f"Input : {repr(SAMPLE_TEXT)}")
    print(f"Output: {tokens}\n")


def demo_clean():
    """Demo tokenize sạch — xoá dấu câu."""
    print("=" * 60)
    print("DEMO: Clean Tokenize (xoá dấu câu)")
    print("=" * 60)

    # Lưu ý: WhitespaceTokenizer KHÔNG đổi, chỉ đổi strategy trong config
    config = TokenizerConfig(
        strategy=CleanTokenizeStrategy(),
        lowercase=True,
        count_frequency=False,
    )

    tokenizer = WhitespaceTokenizer()
    tokens = tokenizer.run(SAMPLE_TEXT, config)
    print(f"Input : {repr(SAMPLE_TEXT)}")
    print(f"Output: {tokens}\n")


def demo_frequency():
    """Demo đếm tần suất token."""
    print("=" * 60)
    print("DEMO: Token Frequency Count")
    print("=" * 60)

    text = "the cat sat on the mat the cat"
    config = TokenizerConfig(
        strategy=CleanTokenizeStrategy(),
        lowercase=True,
        count_frequency=True,
    )

    tokenizer = WhitespaceTokenizer()
    freq = tokenizer.run(text, config)
    print(f"Input : {repr(text)}")
    print(f"Output: {freq}\n")


def demo_batch():
    """Demo batch tokenization."""
    print("=" * 60)
    print("DEMO: Batch Tokenization")
    print("=" * 60)

    config = TokenizerConfig(
        strategy=BasicTokenizeStrategy(),
        lowercase=True,
    )

    tokenizer = WhitespaceTokenizer()
    results = tokenizer.run_batch(BATCH_TEXTS, config)
    for text, tokens in zip(BATCH_TEXTS, results):
        print(f"  {repr(text):30s} → {tokens}")
    print()


if __name__ == "__main__":
    demo_basic()
    demo_clean()
    demo_frequency()
    demo_batch()