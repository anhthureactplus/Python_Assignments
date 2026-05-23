"""
strategies/base.py — Abstract base class cho mọi clean strategy.

OOP Principle: ABSTRACTION
─────────────────────────────
CleanStrategy định nghĩa hợp đồng (contract) mà mọi chiến lược làm sạch
văn bản phải tuân thủ. Nó KHÔNG implement chi tiết — chỉ phơi ra interface.

Decorator @abstractmethod buộc subclass phải override method `clean()`,
và bản thân CleanStrategy không thể được khởi tạo trực tiếp.
"""

from abc import ABC, abstractmethod


class CleanStrategy(ABC):
    """
    Interface cho các chiến lược làm sạch văn bản.

    Mọi subclass phải implement method `clean()` với chữ ký này.
    """

    @abstractmethod
    def clean(self, text: str) -> str:
        """
        Làm sạch văn bản đầu vào.

        Args:
            text: chuỗi văn bản thô

        Returns:
            chuỗi đã được làm sạch theo chiến lược cụ thể
        """
        pass
