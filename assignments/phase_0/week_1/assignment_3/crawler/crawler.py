"""
crawler.py — Main WebCrawler class (Context trong Strategy Pattern).

OOP Principles:
  - ABSTRACTION: method `run()` ẩn toàn bộ workflow phức tạp
    (tạo fetcher, lọc domain, dispatch sang strategy) sau một lời gọi đơn
  - POLYMORPHISM: gọi config.deep_crawl_strategy.crawl() mà KHÔNG cần biết
    strategy cụ thể là BFS, DFS, hay bất kỳ subclass nào khác
"""

from urllib.parse import urlparse
import requests
from crawler.config import CrawlerRunConfig


class WebCrawler:
    """
    Crawler chính — đóng vai trò Context trong Strategy Pattern.

    Không tự thực hiện thuật toán crawl mà uỷ thác cho strategy
    được chỉ định trong config.
    """

    def run(self, url: str, config: CrawlerRunConfig) -> list[dict]:
        """
        Chạy crawler với cấu hình cho trước.

        Người gọi chỉ cần truyền url và config — không cần biết bên trong:
          - fetcher được tạo như thế nào
          - domain filter hoạt động ra sao
          - strategy nào đang được dùng
        """
        start_domain = urlparse(url).netloc

        def fetcher(page_url: str) -> str | None:
            """
            Closure: tải HTML từ URL, áp dụng filter domain nếu cần.

            Đây là một closure (đóng), capture `start_domain` và `config`
            từ scope bên ngoài. Nó được truyền vào strategy như một dependency.
            """
            if config.same_domain_only:
                if urlparse(page_url).netloc != start_domain:
                    return None
            try:
                resp = requests.get(
                    page_url,
                    headers=config.headers,
                    timeout=config.timeout,
                )
                resp.raise_for_status()
                return resp.text
            except Exception as exc:
                print(f"[skip] {page_url} — {exc}")
                return None

        # ★ Đây là điểm POLYMORPHISM thực sự:
        # WebCrawler không biết strategy là BFS hay DFS,
        # Python tự dispatch đến đúng implementation tại runtime.
        return config.deep_crawl_strategy.crawl(
            start_url=url,
            max_depth=config.max_depth,
            max_pages=config.max_pages,
            fetcher=fetcher,
        )
