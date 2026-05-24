from typing import Tuple

import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split

from text_classifier.config import Config
from text_classifier.utils import preprocess_texts


class DatasetLoader:
    """Load and prepare Hugging Face dataset for text classification."""

    def __init__(self, config: Config = Config):
        self.config = config

    def load(self) -> Tuple[list, list, list, list]:
        dataset = load_dataset(self.config.DATASET_NAME)
        df = self._to_dataframe(dataset)

        text_col = self._find_column(df, self.config.TEXT_COLUMN_CANDIDATES)
        label_col = self._find_column(df, self.config.LABEL_COLUMN_CANDIDATES)

        df = df[[text_col, label_col]].dropna()

        if self.config.MAX_SAMPLES is not None and len(df) > self.config.MAX_SAMPLES:
            df = df.sample(self.config.MAX_SAMPLES, random_state=self.config.RANDOM_STATE)

        texts = preprocess_texts(df[text_col].tolist())
        labels = df[label_col].tolist()

        return train_test_split(
            texts,
            labels,
            test_size=self.config.TEST_SIZE,
            random_state=self.config.RANDOM_STATE,
            stratify=labels if len(set(labels)) > 1 else None,
        )

    def _to_dataframe(self, dataset) -> pd.DataFrame:
        if "train" in dataset:
            return dataset["train"].to_pandas()

        first_split = list(dataset.keys())[0]
        return dataset[first_split].to_pandas()

    def _find_column(self, df: pd.DataFrame, candidates: list) -> str:
        for col in candidates:
            if col in df.columns:
                return col

        raise ValueError(
            f"Không tìm thấy cột phù hợp. Các cột hiện có: {list(df.columns)}"
        )
