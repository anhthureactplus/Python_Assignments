"""
main.py — Demo cách sử dụng package encoder.

Minh hoạ POLYMORPHISM: cùng OneHotEncoder, chỉ đổi strategy trong config
là có vocab khác nhau (Basic vs SpecialToken), KHÔNG sửa gì trong encoder.
"""

import numpy as np
from encoder import (
    OneHotEncoder,
    EncoderConfig,
    BasicVocabStrategy,
    SpecialTokenVocabStrategy,
)

SENTENCES = [
    "I love NLP",
    "NLP is fun",
]


def demo_basic():
    """Demo one-hot encoding cơ bản — đúng yêu cầu đề bài."""
    print("=" * 60)
    print("DEMO: Basic One-Hot Encoding")
    print("=" * 60)

    config = EncoderConfig(
        strategy=BasicVocabStrategy(),
        lowercase=True,
    )

    encoder = OneHotEncoder()
    encoder.fit(SENTENCES, config)

    print(f"\nVocabulary ({encoder.vocab_size} words):")
    for word, idx in encoder.vocab.items():
        print(f"  '{word}': {idx}")

    print("\nOne-hot vectors:")
    for word in encoder.vocab:
        vec = encoder.encode_word(word)
        print(f"  '{word}' -> {vec.tolist()}")

    print("\nEncoded sentence 'I love NLP':")
    matrix = encoder.encode_sentence("I love NLP")
    print(f"  Shape: {matrix.shape}")
    print(f"  Matrix:\n{matrix}\n")


def demo_special_tokens():
    """Demo với <UNK> và <PAD> (Bonus)."""
    print("=" * 60)
    print("DEMO: Special Tokens <UNK> + <PAD> (Bonus)")
    print("=" * 60)

    config = EncoderConfig(
        strategy=SpecialTokenVocabStrategy(),
        lowercase=True,
        add_unk=True,
        add_pad=True,
        padding_length=5,
    )

    encoder = OneHotEncoder()
    encoder.fit(SENTENCES, config)

    print(f"\nVocabulary ({encoder.vocab_size} words):")
    for word, idx in encoder.vocab.items():
        print(f"  '{word}': {idx}")

    print("\nUnknown word 'deep' → <UNK>:")
    vec = encoder.encode_word("deep")
    print(f"  'deep' -> {vec.tolist()}")

    print("\nEncoded + padded sentence 'NLP is fun' (length=5):")
    matrix = encoder.encode_sentence("NLP is fun")
    print(f"  Shape: {matrix.shape}")
    print(f"  Matrix:\n{matrix}\n")


def demo_batch():
    """Demo batch encoding."""
    print("=" * 60)
    print("DEMO: Batch Encoding")
    print("=" * 60)

    config = EncoderConfig(
        strategy=BasicVocabStrategy(),
        lowercase=True,
    )

    encoder = OneHotEncoder()
    encoder.fit(SENTENCES, config)

    results = encoder.encode_batch(SENTENCES)
    for sentence, matrix in zip(SENTENCES, results):
        print(f"\n  '{sentence}'")
        print(f"  Shape: {matrix.shape}")
        print(f"  Matrix:\n{matrix}")
    print()


if __name__ == "__main__":
    demo_basic()
    demo_special_tokens()
    demo_batch()
