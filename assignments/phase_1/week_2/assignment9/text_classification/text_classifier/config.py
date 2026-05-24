class Config:
    DATASET_NAME = "clapAI/MultiLingualSentiment"
    TEXT_COLUMN_CANDIDATES = ["text", "sentence", "content", "review"]
    LABEL_COLUMN_CANDIDATES = ["label", "labels", "sentiment"]

    TEST_SIZE = 0.2
    RANDOM_STATE = 42
    MAX_FEATURES = 5000

    # Dùng để chạy nhanh khi máy yếu. Đặt None nếu muốn dùng toàn bộ dataset.
    MAX_SAMPLES = 20000
