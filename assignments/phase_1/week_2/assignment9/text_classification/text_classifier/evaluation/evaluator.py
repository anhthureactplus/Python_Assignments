from sklearn.metrics import accuracy_score, f1_score


class Evaluator:
    """Evaluate classification results."""

    def evaluate(self, y_true, y_pred) -> dict:
        return {
            "accuracy": accuracy_score(y_true, y_pred),
            "f1_score": f1_score(y_true, y_pred, average="weighted", zero_division=0),
        }
