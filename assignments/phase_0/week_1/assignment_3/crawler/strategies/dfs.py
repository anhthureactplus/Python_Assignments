"""
strategies/dfs.py — Depth-First Search crawl strategy.

OOP Principles:
  - INHERITANCE: kế thừa từ DeepCrawlStrategy, tái sử dụng interface chung
  - POLYMORPHISM: cùng method `crawl` nhưng triển khai theo chiều sâu
  - ENCAPSULATION: method `_dfs` (prefix _) là helper nội bộ, không phơi ra ngoài
"""

from .base import DeepCrawlStrategy
from crawler.utils import extract_links


class DFSDeepCrawlStrategy(DeepCrawlStrategy):
    """
    Chiến lược crawl theo chiều sâu (Depth-First Search).

    Đi sâu vào một nhánh trước khi quay lại nhánh khác.
    Phù hợp khi cần khám phá kỹ một đường dẫn cụ thể.
    """

    def crawl(self, start_url, max_depth, max_pages, fetcher):
        results = []
        visited: set[str] = set()
        self._dfs(start_url, 0, max_depth, max_pages, fetcher, visited, results)
        return results

    def _dfs(self, url, depth, max_depth, max_pages, fetcher, visited, results):
        """
        Helper đệ quy nội bộ.

        Prefix `_` báo hiệu method này là implementation detail,
        không nên gọi từ bên ngoài class.
        """
        if url in visited or len(results) >= max_pages:
            return
        visited.add(url)

        html = fetcher(url)
        if html is None:
            return

        results.append({"url": url, "depth": depth, "html": html})

        if depth < max_depth:
            for link in extract_links(html, url):
                if len(results) >= max_pages:
                    break
                self._dfs(link, depth + 1, max_depth, max_pages, fetcher, visited, results)
