"""
main.py — Demo cách sử dụng package processor.

File này minh hoạ POLYMORPHISM trong thực tế: cùng một VietnameseTextProcessor,
chỉ cần đổi strategy trong config là có hành vi làm sạch khác nhau,
KHÔNG cần sửa bất kỳ dòng nào trong VietnameseTextProcessor.preprocess().
"""

from assignments.phase_1.week_2.assignment2.processor.processor import (
    VietnameseTextProcessor,
    ProcessorConfig,
    BasicCleanStrategy,
    AggressiveCleanStrategy,
)

SAMPLE_TEXT = """<p>Hello!!!</p>
I am learning NLP 😄
Visit https://abc.com now!!!
"""

VIETNAMESE_TEXT = """<b>Xử lý ngôn ngữ tự nhiên</b> là một lĩnh vực của AI 🤖
Truy cập https://underthesea.vn để biết thêm!!!
Tôi đang học và nghiên cứu NLP.
"""


def demo_basic():
    """Demo pipeline cơ bản — chỉ xoá HTML, giữ URL và emoji."""
    print("=" * 60)
    print("DEMO: Basic Clean Strategy")
    print("=" * 60)

    config = ProcessorConfig(
        clean_strategy=BasicCleanStrategy(),
        lowercase=True,
        remove_stopwords=False,
    )

    processor = VietnameseTextProcessor()
    result = processor.preprocess(SAMPLE_TEXT, config)

    print(f"Sentences      : {result['sentences']}")
    print(f"Tokens         : {result['tokens']}")
    print(f"Processed text : {result['processed_text']}\n")


def demo_aggressive():
    """Demo pipeline toàn diện — xoá HTML, URL, emoji, dấu câu."""
    print("=" * 60)
    print("DEMO: Aggressive Clean Strategy")
    print("=" * 60)

    # Lưu ý: VietnameseTextProcessor KHÔNG đổi, chỉ đổi strategy trong config
    config = ProcessorConfig(
        clean_strategy=AggressiveCleanStrategy(),
        lowercase=True,
        remove_stopwords=False,
    )

    processor = VietnameseTextProcessor()
    result = processor.preprocess(SAMPLE_TEXT, config)

    print(f"Sentences      : {result['sentences']}")
    print(f"Tokens         : {result['tokens']}")
    print(f"Processed text : {result['processed_text']}\n")


def demo_stopwords():
    """Demo với stopword removal — dùng file .txt (Bonus)."""
    print("=" * 60)
    print("DEMO: Aggressive + Stopword Removal (load từ file)")
    print("=" * 60)

    config = ProcessorConfig(
        clean_strategy=AggressiveCleanStrategy(),
        lowercase=True,
        remove_stopwords=True,
        stopwords_path="stopwords.txt",  # Bonus: load từ file
    )

    processor = VietnameseTextProcessor()
    result = processor.preprocess(SAMPLE_TEXT, config)

    print(f"Sentences      : {result['sentences']}")
    print(f"Tokens         : {result['tokens']}")
    print(f"Processed text : {result['processed_text']}\n")


def demo_vietnamese():
    """Demo với văn bản tiếng Việt thực tế."""
    print("=" * 60)
    print("DEMO: Vietnamese Text")
    print("=" * 60)

    config = ProcessorConfig(
        clean_strategy=AggressiveCleanStrategy(),
        lowercase=True,
        remove_stopwords=True,
        stopwords_path="stopwords.txt",
    )

    processor = VietnameseTextProcessor()
    result = processor.preprocess(VIETNAMESE_TEXT, config)

    print(f"Sentences      : {result['sentences']}")
    print(f"Tokens         : {result['tokens']}")
    print(f"Processed text : {result['processed_text']}\n")


if __name__ == "__main__":
    demo_basic()
    demo_aggressive()
    demo_stopwords()
    demo_vietnamese()