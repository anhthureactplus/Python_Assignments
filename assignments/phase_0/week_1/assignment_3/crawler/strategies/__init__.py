"""
strategies — Sub-package chứa các chiến lược crawl.

Mỗi strategy nằm trong file riêng để:
  - Dễ thêm strategy mới mà không sửa file hiện có (Open/Closed Principle)
  - Cô lập logic của từng thuật toán
"""

from Python_Assignments.assignments.phase_0.week_1.assignment_3.crawler.strategies.base import DeepCrawlStrategy
from Python_Assignments.assignments.phase_0.week_1.assignment_3.crawler.strategies.bfs import BFSDeepCrawlStrategy
from Python_Assignments.assignments.phase_0.week_1.assignment_3.crawler.strategies.dfs import DFSDeepCrawlStrategy

__all__ = [
    "DeepCrawlStrategy",
    "BFSDeepCrawlStrategy",
    "DFSDeepCrawlStrategy",
]
