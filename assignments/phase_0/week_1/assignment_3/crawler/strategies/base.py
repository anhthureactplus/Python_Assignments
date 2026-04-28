"""
strategies/base.py — Abstract base class cho mọi crawl strategy.

OOP Principle: ABSTRACTION
─────────────────────────────
DeepCrawlStrategy là một abstract base class (ABC) định nghĩa hợp đồng
(contract) mà mọi chiến lược crawl phải tuân thủ. Nó KHÔNG implement
chi tiết — chỉ phơi ra interface "cái gì cần làm".

Decorator @abstractmethod buộc subclass phải override method `crawl()`,
và bản thân DeepCrawlStrategy không thể được khởi tạo trực tiếp.
"""

from abc import ABC, abstractmethod
from typing import Callable


class DeepCrawlStrategy(ABC):
    """
    Interface cho các chiến lược crawl sâu (deep crawl).

    Mọi subclass phải implement method `crawl()` với chữ ký này.
    """

    @abstractmethod
    def crawl(
        self,
        start_url: str,
        max_depth: int,
        max_pages: int,
        fetcher: Callable[[str], str | None],
    ) -> list[dict]:
        """
        Thực hiện crawl bắt đầu từ start_url.

        Args:
            start_url: URL khởi điểm
            max_depth: độ sâu tối đa
            max_pages: số trang tối đa
            fetcher: callable nhận URL, trả về HTML hoặc None

        Returns:
            list các dict {"url": ..., "depth": ..., "html": ...}
        """
        pass
