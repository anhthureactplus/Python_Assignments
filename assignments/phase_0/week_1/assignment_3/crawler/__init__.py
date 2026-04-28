"""
web_crawler — A modular web crawler demonstrating OOP principles.

Public API:
    - WebCrawler: main crawler class
    - CrawlerRunConfig: configuration object
    - DeepCrawlStrategy: abstract base for strategies
    - BFSDeepCrawlStrategy, DFSDeepCrawlStrategy: concrete strategies
"""

from .crawler import WebCrawler
from .config import CrawlerRunConfig
from Python_Assignments.assignments.phase_0.week_1.assignment_3.crawler.strategies import (
    DeepCrawlStrategy,
    BFSDeepCrawlStrategy,
    DFSDeepCrawlStrategy,
)

__all__ = [
    "WebCrawler",
    "CrawlerRunConfig",
    "DeepCrawlStrategy",
    "BFSDeepCrawlStrategy",
    "DFSDeepCrawlStrategy",
]
