"""
tokenizer.py — Main WhitespaceTokenizer class (Context trong Strategy Pattern).

OOP Principles:
  - ABSTRACTION: method `run()` ẩn toàn bộ workflow phức tạp
    (lowercase → normalize → tokenize → đếm tần suất) sau một lời gọi đơn
  - POLYMORPHISM: gọi config.strategy.tokenize() mà KHÔNG cần biết
    strategy cụ thể là Basic, Clean, hay bất kỳ subclass nào khác
"""

from tokenizer.config import TokenizerConfig
from tokenizer.utils import lowercase, normalize_whitespace, count_frequency


class WhitespaceTokenizer:
    """
    Tokenizer chính — đóng vai trò Context trong Strategy Pattern.

    Không tự thực hiện thuật toán tách token mà uỷ thác cho strategy
    được chỉ định trong config.
    """

    def run(self, text: str, config: TokenizerConfig) -> list[str] | dict[str, int]:
        """
        Chạy tokenizer với cấu hình cho trước.

        Người gọi chỉ cần truyền text và config — không cần biết bên trong:
          - lowercase xảy ra ở đâu
          - normalize hoạt động ra sao
          - strategy nào đang được dùng

        Args:
            text: văn bản đầu vào
            config: cấu hình tokenizer

        Returns:
            list[str] nếu config.count_frequency = False
            dict[str, int] nếu config.count_frequency = True
        """
        # Bước 1: lowercase (nếu được bật)
        if config.lowercase:
            text = lowercase(text)

        # Bước 2: chuẩn hoá khoảng trắng (luôn chạy)
        text = normalize_whitespace(text)

        # ★ Đây là điểm POLYMORPHISM thực sự:
        # WhitespaceTokenizer không biết strategy là Basic hay Clean,
        # Python tự dispatch đến đúng implementation tại runtime.
        tokens = config.strategy.tokenize(text)

        # Bước 4 (tuỳ chọn): đếm tần suất
        if config.count_frequency:
            return count_frequency(tokens)

        return tokens

    def run_batch(
        self, texts: list[str], config: TokenizerConfig
    ) -> list[list[str]] | list[dict[str, int]]:
        """
        Tokenize nhiều văn bản cùng lúc (Bonus: Batch Tokenization).

        Args:
            texts: danh sách văn bản đầu vào
            config: cấu hình dùng chung cho tất cả

        Returns:
            list kết quả tokenize cho từng văn bản
        """
        return [self.run(text, config) for text in texts]