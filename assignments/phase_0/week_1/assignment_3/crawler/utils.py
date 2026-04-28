"""
utils.py — Helper functions chung cho toàn package.

Module này KHÔNG chứa class OOP nào — chỉ là pure functions.
Việc tách helper ra module riêng giúp:
  - Tái sử dụng giữa các strategy khác nhau
  - Dễ test độc lập
  - Tránh ô nhiễm namespace của các module chính
"""

from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup


def extract_links(html: str, base_url: str) -> list[str]:
    """
    Trích xuất tất cả liên kết HTTP/HTTPS từ HTML.

    Args:
        html: nội dung HTML cần parse
        base_url: URL gốc để resolve các đường dẫn tương đối

    Returns:
        list các URL tuyệt đối (đã loại fragment #...)
    """
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"].split("#")[0]  # bỏ fragment
        absolute = urljoin(base_url, href)
        parsed = urlparse(absolute)
        if parsed.scheme in ("http", "https"):
            links.append(absolute)
    return links
