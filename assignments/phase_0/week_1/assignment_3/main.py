"""
main.py — Demo cách sử dụng package web_crawler.

File này minh hoạ POLYMORPHISM trong thực tế: cùng một WebCrawler,
chỉ cần đổi strategy trong config là có hành vi crawl khác nhau,
KHÔNG cần sửa bất kỳ dòng nào trong WebCrawler.run().
"""

from crawler import (
    WebCrawler,
    CrawlerRunConfig,
    BFSDeepCrawlStrategy,
    DFSDeepCrawlStrategy,
)


def demo_bfs():
    """Demo crawl theo chiều rộng."""
    print("=" * 60)
    print("DEMO: BFS Crawl")
    print("=" * 60)

    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(),
        max_depth=2,
        max_pages=10,
        same_domain_only=True,
    )

    crawler = WebCrawler()
    results = crawler.run("https://example.com", config)

    for page in results:
        print(f"  [depth={page['depth']}] {page['url']}")
    print(f"Tổng số trang: {len(results)}\n")


def demo_dfs():
    """Demo crawl theo chiều sâu — chỉ cần đổi strategy."""
    print("=" * 60)
    print("DEMO: DFS Crawl")
    print("=" * 60)

    # Lưu ý: WebCrawler KHÔNG đổi, chỉ đổi strategy trong config
    config = CrawlerRunConfig(
        deep_crawl_strategy=DFSDeepCrawlStrategy(),
        max_depth=2,
        max_pages=10,
        same_domain_only=True,
    )

    crawler = WebCrawler()
    results = crawler.run("https://example.com", config)

    for page in results:
        print(f"  [depth={page['depth']}] {page['url']}")
    print(f"Tổng số trang: {len(results)}\n")


if __name__ == "__main__":
    demo_bfs()
    demo_dfs()
