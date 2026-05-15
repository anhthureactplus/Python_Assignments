"""
encoder.py — Main OneHotEncoder class (Context trong Strategy Pattern).

OOP Principles:
  - ABSTRACTION : method `fit()` và `encode()` ẩn toàn bộ chi tiết
  - POLYMORPHISM: gọi config.strategy.build_vocab() mà không cần biết
    strategy là Basic hay SpecialToken
"""

import numpy as np

from encoder.config import EncoderConfig
from encoder.utils import lowercase, tokenize, make_one_hot, pad_matrix
from encoder.strategies.special import PAD_TOKEN, UNK_TOKEN


class OneHotEncoder:
    """
    Encoder chính — đóng vai trò Context trong Strategy Pattern.

    Workflow:
        1. fit()    — học vocab từ corpus
        2. encode() — chuyển câu thành ma trận one-hot
    """

    def __init__(self):
        self.vocab: dict[str, int] = {}
        self.vocab_size: int = 0
        self._config: EncoderConfig | None = None

    def fit(self, sentences: list[str], config: EncoderConfig) -> "OneHotEncoder":
        """
        Học vocabulary từ danh sách câu.

        ★ POLYMORPHISM: gọi config.strategy.build_vocab() — không biết
          strategy cụ thể là gì, Python tự dispatch tại runtime.

        Args:
            sentences: danh sách câu đầu vào
            config   : cấu hình encoder

        Returns:
            self (để chain: encoder.fit(...).encode(...))
        """
        self._config = config

        # Lowercase trước khi build vocab (nếu bật)
        processed = [lowercase(s) for s in sentences] if config.lowercase else sentences

        # ★ Đây là điểm POLYMORPHISM
        self.vocab = config.strategy.build_vocab(processed)
        self.vocab_size = len(self.vocab)
        return self

    def encode_word(self, word: str) -> np.ndarray:
        """
        Chuyển một từ thành one-hot vector.

        Args:
            word: từ cần encode (đã lowercase nếu cần)

        Returns:
            numpy array shape (vocab_size,)

        Example:
            >>> encoder.encode_word("love")
            array([0, 1, 0, 0, 0])
        """
        if word in self.vocab:
            index = self.vocab[word]
        elif UNK_TOKEN in self.vocab:
            # Bonus: từ lạ → dùng <UNK>
            index = self.vocab[UNK_TOKEN]
        else:
            raise KeyError(f"'{word}' không có trong vocab và không có <UNK>.")

        return make_one_hot(index, self.vocab_size)

    def encode_sentence(self, sentence: str) -> np.ndarray:
        """
        Chuyển một câu thành ma trận one-hot.

        Args:
            sentence: câu đầu vào

        Returns:
            numpy array shape (n_tokens, vocab_size)
        """
        if self._config and self._config.lowercase:
            sentence = lowercase(sentence)

        tokens = tokenize(sentence)
        matrix = np.array([self.encode_word(t) for t in tokens])

        # Bonus: padding về độ dài cố định
        if (
            self._config
            and self._config.add_pad
            and self._config.padding_length
            and PAD_TOKEN in self.vocab
        ):
            matrix = pad_matrix(matrix, self._config.padding_length, self.vocab[PAD_TOKEN])

        return matrix

    def encode_batch(self, sentences: list[str]) -> list[np.ndarray]:
        """
        Chuyển nhiều câu thành danh sách ma trận one-hot.

        Args:
            sentences: danh sách câu

        Returns:
            list các ma trận one-hot
        """
        return [self.encode_sentence(s) for s in sentences]
