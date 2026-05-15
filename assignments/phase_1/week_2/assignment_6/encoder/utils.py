"""
utils.py — Helper functions chung cho toàn package.

Pure functions — không có side effect, dễ test độc lập.
"""

import numpy as np


def lowercase(text: str) -> str:
    """
    Chuyển toàn bộ text về chữ thường.

    Example:
        >>> lowercase("I Love NLP")
        'i love nlp'
    """
    return text.lower()


def tokenize(text: str) -> list[str]:
    """
    Tách text thành danh sách token bằng whitespace.

    Example:
        >>> tokenize("i love nlp")
        ['i', 'love', 'nlp']
    """
    return text.split()


def make_one_hot(index: int, vocab_size: int) -> np.ndarray:
    """
    Tạo one-hot vector cho một index cho trước.

    Args:
        index     : vị trí của từ trong vocab
        vocab_size: kích thước vocab (độ dài vector)

    Returns:
        numpy array shape (vocab_size,) với giá trị 1 tại index, 0 ở nơi khác

    Example:
        >>> make_one_hot(1, 5)
        array([0, 1, 0, 0, 0])
    """
    vector = np.zeros(vocab_size, dtype=int)
    vector[index] = 1
    return vector


def pad_matrix(matrix: np.ndarray, length: int, pad_index: int) -> np.ndarray:
    """
    Padding hoặc truncate ma trận one-hot về đúng số hàng = length.

    Args:
        matrix   : ma trận one-hot shape (n_tokens, vocab_size)
        length   : số hàng mong muốn
        pad_index: index của token <PAD> trong vocab

    Returns:
        ma trận shape (length, vocab_size)

    Bonus: hỗ trợ padding cố định.
    """
    vocab_size = matrix.shape[1]
    if len(matrix) >= length:
        return matrix[:length]

    pad_rows = length - len(matrix)
    pad_vector = np.zeros((pad_rows, vocab_size), dtype=int)
    pad_vector[:, pad_index] = 1
    return np.vstack([matrix, pad_vector])
