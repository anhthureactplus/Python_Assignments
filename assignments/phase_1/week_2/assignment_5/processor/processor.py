"""
processor.py — Main VietnameseTextProcessor class (Context trong Strategy Pattern).

OOP Principles:
  - ABSTRACTION : method `preprocess()` ẩn toàn bộ pipeline phức tạp
    (sentence split → clean → lowercase → word tokenize → stopword filter)
    sau một lời gọi đơn
  - POLYMORPHISM: gọi config.clean_strategy.clean() mà KHÔNG cần biết
    strategy cụ thể là Basic, Aggressive, hay bất kỳ subclass nào khác
"""

from underthesea import sent_tokenize, word_tokenize

from processor.config import ProcessorConfig
from processor.utils import lowercase, load_stopwords, filter_stopwords


class VietnameseTextProcessor:
    """
    Processor chính — đóng vai trò Context trong Strategy Pattern.

    Không tự thực hiện thuật toán làm sạch mà uỷ thác cho strategy
    được chỉ định trong config.
    """

    def sentence_tokenize(self, text: str) -> list[str]:
        """
        Tách văn bản thành danh sách câu bằng underthesea.

        Args:
            text: văn bản thô đầu vào

        Returns:
            list các câu

        Example:
            >>> processor.sentence_tokenize("Xin chào! Tôi học NLP.")
            ['Xin chào!', 'Tôi học NLP.']
        """
        return sent_tokenize(text)

    def word_tokenize(self, text: str) -> list[str]:
        """
        Tách văn bản thành danh sách token từ bằng underthesea.
        Hỗ trợ tiếng Việt (từ ghép: "xử lý", "ngôn ngữ", ...).

        Args:
            text: chuỗi đã được làm sạch

        Returns:
            list các token

        Example:
            >>> processor.word_tokenize("xử lý ngôn ngữ tự nhiên")
            ['xử lý', 'ngôn ngữ', 'tự nhiên']
        """
        return word_tokenize(text)

    def preprocess(self, text: str, config: ProcessorConfig) -> dict:
        """
        Chạy toàn bộ pipeline với cấu hình cho trước.

        Người gọi chỉ cần truyền text và config — không cần biết bên trong:
          - strategy nào đang làm sạch
          - stopwords được load từ đâu
          - word tokenize dùng thư viện gì

        Pipeline:
            1. Sentence tokenize (trước khi làm sạch để giữ cấu trúc câu)
            2. Làm sạch văn bản (uỷ thác cho strategy — POLYMORPHISM)
            3. Lowercase (nếu bật)
            4. Word tokenize
            5. Loại stopwords (nếu bật)

        Args:
            text  : văn bản thô đầu vào
            config: cấu hình pipeline

        Returns:
            dict gồm:
              - "sentences"     : list câu gốc
              - "tokens"        : list token sau khi xử lý
              - "processed_text": chuỗi cuối cùng join từ tokens
        """
        # Bước 1: tách câu từ văn bản gốc (giữ nguyên, chưa làm sạch)
        sentences = self.sentence_tokenize(text)

        # ★ Bước 2: POLYMORPHISM —
        # VietnameseTextProcessor không biết strategy là Basic hay Aggressive,
        # Python tự dispatch đến đúng implementation tại runtime.
        cleaned = config.clean_strategy.clean(text)

        # Bước 3: lowercase (nếu được bật)
        if config.lowercase:
            cleaned = lowercase(cleaned)

        # Bước 4: word tokenize
        tokens = self.word_tokenize(cleaned)

        # Bước 5: loại stopwords (nếu được bật)
        if config.remove_stopwords:
            stopwords = set()
            if config.stopwords_path:
                # Bonus: load từ file .txt
                stopwords = load_stopwords(config.stopwords_path)
            else:
                # Stopwords tiếng Việt mặc định
                stopwords = _DEFAULT_VIETNAMESE_STOPWORDS
            tokens = filter_stopwords(tokens, stopwords)

        return {
            "sentences": sentences,
            "tokens": tokens,
            "processed_text": " ".join(tokens),
        }


# ---------------------------------------------------------------------------
# Stopwords tiếng Việt mặc định (dùng khi không có file .txt)
# ---------------------------------------------------------------------------
_DEFAULT_VIETNAMESE_STOPWORDS: set[str] = {
    "và", "hoặc", "nhưng", "mà", "thì", "là", "của", "cho",
    "với", "về", "trong", "ngoài", "trên", "dưới", "từ", "đến",
    "tại", "bởi", "vì", "nên", "để", "rằng", "như", "khi",
    "này", "đó", "kia", "ấy", "các", "những", "mọi", "một",
    "có", "không", "đã", "đang", "sẽ", "được", "bị", "rất",
    "cũng", "vẫn", "còn", "lại", "đây", "đấy", "thế", "vậy",
    "i", "am", "is", "are", "the", "a", "an", "to", "of",
    "in", "on", "at", "by", "for", "with", "and", "or", "but",
}
