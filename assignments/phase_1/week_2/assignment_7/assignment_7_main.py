"""
main.py — Assignment 7: Sentence Representation Using One-Hot

Tái sử dụng package `encoder` từ Assignment 6.
Không viết lại logic — đây là sức mạnh của OOP: code đã có, dùng lại.

Workflow:
    "I love NLP"
        ↓  fit vocab
        ↓  encode_sentence()
    [[1,0,0,0,0],
     [0,1,0,0,0],
     [0,0,1,0,0]]
"""

import sys
import os

# Trỏ đến thư mục assignment_6 để import encoder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "assignment_6"))

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
    """Yêu cầu chính: chuyển câu thành dãy one-hot vector."""
    print("=" * 60)
    print("DEMO: Sentence → Sequence of One-Hot Vectors")
    print("=" * 60)

    config = EncoderConfig(
        strategy=BasicVocabStrategy(),
        lowercase=True,
    )

    encoder = OneHotEncoder()
    encoder.fit(SENTENCES, config)

    sentence = "I love NLP"
    matrix = encoder.encode_sentence(sentence)

    print(f'\nInput : "{sentence}"')
    print(f"\nOutput:")
    print("[")
    for row in matrix:
        print(f"  {row.tolist()},")
    print(f"]")
    print(f"\nShape: {matrix.shape}  ({matrix.shape[0]} tokens × {matrix.shape[1]} vocab size)\n")


def demo_truncation():
    """Bonus: truncation — cắt bớt nếu câu dài hơn max_length."""
    print("=" * 60)
    print("BONUS: Truncation (max_length=2)")
    print("=" * 60)

    config = EncoderConfig(
        strategy=SpecialTokenVocabStrategy(),
        lowercase=True,
        add_pad=True,
        padding_length=2,   # truncate về 2 token
    )

    encoder = OneHotEncoder()
    encoder.fit(SENTENCES, config)

    sentence = "I love NLP"
    matrix = encoder.encode_sentence(sentence)

    print(f'\nInput : "{sentence}" (3 tokens → truncate còn 2)')
    print(f"\nOutput:")
    print("[")
    for row in matrix:
        print(f"  {row.tolist()},")
    print(f"]")
    print(f"\nShape: {matrix.shape}\n")


def demo_padding():
    """Bonus: padding — thêm <PAD> nếu câu ngắn hơn max_length."""
    print("=" * 60)
    print("BONUS: Padding (max_length=6)")
    print("=" * 60)

    config = EncoderConfig(
        strategy=SpecialTokenVocabStrategy(),
        lowercase=True,
        add_pad=True,
        padding_length=6,   # pad lên 6 token
    )

    encoder = OneHotEncoder()
    encoder.fit(SENTENCES, config)

    sentence = "NLP is fun"
    matrix = encoder.encode_sentence(sentence)

    print(f'\nInput : "{sentence}" (3 tokens → pad lên 6)')
    print(f"\nOutput:")
    print("[")
    for i, row in enumerate(matrix):
        label = "← <PAD>" if i >= 3 else ""
        print(f"  {row.tolist()},  {label}")
    print(f"]")
    print(f"\nShape: {matrix.shape}\n")


if __name__ == "__main__":
    demo_basic()
    demo_truncation()
    demo_padding()
