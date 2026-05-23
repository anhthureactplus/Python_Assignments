from tf.config import TFConfig
from tf.utils import lowercase, tokenize


class TFCalculator:
    """
    Calculator chính — điều phối tokenize và tính TF theo strategy.
    """

    def compute(self, document: str, config: TFConfig) -> dict[str, float]:
        """
        Tính TF cho một document.

        Args:
            document: văn bản đầu vào
            config  : cấu hình TF

        Returns:
            dict ánh xạ token → TF score
        """
        if config.lowercase:
            document = lowercase(document)
        tokens = tokenize(document)
        return config.strategy.compute(tokens)

    def compute_batch(self, documents: list[str], config: TFConfig) -> list[dict[str, float]]:
        """
        Tính TF cho nhiều document cùng lúc.
        """
        return [self.compute(doc, config) for doc in documents]
