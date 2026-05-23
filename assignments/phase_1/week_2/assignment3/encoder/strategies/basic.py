"""
strategies/basic.py — Chiến lược xây dựng vocab cơ bản.

OOP Principles:
  - INHERITANCE : kế thừa từ VocabStrategy
  - POLYMORPHISM: cùng method `build_vocab` nhưng KHÔNG có special tokens
"""

from .base import VocabStrategy
from encoder.utils import tokenize


class BasicVocabStrategy(VocabStrategy):
    """
    Chiến lược vocab đơn giản: chỉ gồm các từ xuất hiện trong corpus.

    Không có <UNK> hay <PAD>.
    Phù hợp khi corpus đã biết trước, không có từ lạ.
    """

    def build_vocab(self, sentences: list[str]) -> dict[str, int]:
        """
        Duyệt qua tất cả câu, thu thập từ duy nhất và gán index.

        Example:
            >>> BasicVocabStrategy().build_vocab(["i love nlp", "nlp is fun"])
            {'i': 0, 'love': 1, 'nlp': 2, 'is': 3, 'fun': 4}
        """
        vocab: dict[str, int] = {}
        for sentence in sentences:
            for token in tokenize(sentence):
                if token not in vocab:
                    vocab[token] = len(vocab)
        return vocab
