"""
strategies/special.py — Chiến lược vocab nâng cao: có <UNK> và <PAD>.

OOP Principles:
  - INHERITANCE : kế thừa từ VocabStrategy
  - POLYMORPHISM: cùng method `build_vocab` nhưng thêm special tokens ở đầu
  - ENCAPSULATION: logic đặt <PAD>=0, <UNK>=1 được đóng gói bên trong strategy
"""

from .base import VocabStrategy
from encoder.utils import tokenize

PAD_TOKEN = "<PAD>"
UNK_TOKEN = "<UNK>"


class SpecialTokenVocabStrategy(VocabStrategy):
    """
    Chiến lược vocab nâng cao: đặt <PAD> tại index 0, <UNK> tại index 1
    rồi mới gán index cho các từ thông thường.

    Phù hợp cho các tác vụ NLP thực tế cần xử lý từ lạ và padding.

    Bonus: hỗ trợ <UNK> và <PAD>.
    """

    def build_vocab(self, sentences: list[str]) -> dict[str, int]:
        """
        <PAD>=0, <UNK>=1, các từ thông thường từ index 2 trở đi.

        Example:
            >>> SpecialTokenVocabStrategy().build_vocab(["i love nlp"])
            {'<PAD>': 0, '<UNK>': 1, 'i': 2, 'love': 3, 'nlp': 4}
        """
        # ★ Special tokens luôn ở đầu vocab
        vocab: dict[str, int] = {PAD_TOKEN: 0, UNK_TOKEN: 1}
        for sentence in sentences:
            for token in tokenize(sentence):
                if token not in vocab:
                    vocab[token] = len(vocab)
        return vocab
