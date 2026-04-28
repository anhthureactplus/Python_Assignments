"""
strategies/bfs.py — Breadth-First Search crawl strategy.

OOP Principles:
  - INHERITANCE: kế thừa từ DeepCrawlStrategy, tái sử dụng interface chung
  - POLYMORPHISM: cùng method `crawl` nhưng triển khai theo chiều rộng
"""

from collections import deque
from .base import DeepCrawlStrategy
from crawler.utils import extract_links


class BFSDeepCrawlStrategy(DeepCrawlStrategy):
    """
    Chiến lược crawl theo chiều rộng (Breadth-First Search).

    Duyệt tất cả URL ở depth N trước khi sang depth N+1.
    Phù hợp khi cần coverage rộng và cân bằng giữa các nhánh.
    """

    def crawl(self, start_url, max_depth, max_pages, fetcher):
        results = []
        visited = {start_url}
        # queue chứa các tuple (url, depth)
        queue = deque([(start_url, 0)])

        while queue and len(results) < max_pages:
            url, depth = queue.popleft()

            html = fetcher(url)
            if html is None:
                continue

            results.append({"url": url, "depth": depth, "html": html})

            if depth < max_depth:
                for link in extract_links(html, url):
                    if link not in visited:
                        visited.add(link)
                        queue.append((link, depth + 1))

        return results
