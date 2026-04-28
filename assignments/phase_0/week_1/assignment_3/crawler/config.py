"""
config.py — Configuration object cho WebCrawler.

OOP Principle: ENCAPSULATION
─────────────────────────────
CrawlerRunConfig gói (encapsulate) tất cả các tham số cấu hình liên quan
vào một đơn vị duy nhất. Thay vì truyền 6 tham số rời rạc đi khắp nơi,
ta truyền một config object — dữ liệu đi cùng nhau, dễ quản lý, dễ mở rộng.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

# Tránh circular import: chỉ cần type hint cho DeepCrawlStrategy
if TYPE_CHECKING:
    from Python_Assignments.assignments.phase_0.week_1.assignment_3.crawler.strategies.base import DeepCrawlStrategy


class CrawlerRunConfig:
    """
    Đóng gói cấu hình cho một lần chạy crawler.

    Attributes:
        deep_crawl_strategy: chiến lược crawl (BFS, DFS, ...)
        max_depth: độ sâu tối đa của cây crawl
        max_pages: số trang tối đa thu thập được
        same_domain_only: chỉ crawl các trang cùng domain
        timeout: timeout cho mỗi HTTP request (giây)
        headers: HTTP headers gửi kèm
    """

    def __init__(
        self,
        deep_crawl_strategy: "DeepCrawlStrategy",
        max_depth: int = 2,
        max_pages: int = 50,
        same_domain_only: bool = True,
        timeout: float = 10.0,
        headers: dict | None = None,
    ):
        self.deep_crawl_strategy = deep_crawl_strategy
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.same_domain_only = same_domain_only
        self.timeout = timeout
        self.headers = headers or {"User-Agent": "WebCrawler/1.0"}
