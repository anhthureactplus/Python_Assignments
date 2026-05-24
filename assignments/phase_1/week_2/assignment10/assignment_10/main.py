"""Entry point for Assignment 10: Real-World Search Engine Ranking.

Run examples:
    python main.py --data data --query "python crawler"
    python main.py --data data --query "machine learning" --strategy tfidf --top-k 3
    python main.py --strategy raw
"""

from __future__ import annotations

import argparse

from search_engine import SearchEngine, SearchEngineConfig
from search_engine.strategies import NormalizedTfStrategy, RawCountStrategy, TfidfStrategy


def create_strategy(name: str):
    strategies = {
        "tfidf": TfidfStrategy,
        "normalized": NormalizedTfStrategy,
        "raw": RawCountStrategy,
    }
    try:
        return strategies[name]()
    except KeyError as exc:
        valid = ", ".join(strategies)
        raise ValueError(f"Unknown strategy '{name}'. Choose one of: {valid}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mini TF-IDF search engine ranking system")
    parser.add_argument("--data", default="data", help="Folder containing crawled documents")
    parser.add_argument("--query", default=None, help="Search query. If omitted, interactive mode starts")
    parser.add_argument("--top-k", type=int, default=5, help="Number of ranked results to show")
    parser.add_argument(
        "--strategy",
        choices=["tfidf", "normalized", "raw"],
        default="tfidf",
        help="Vectorization strategy",
    )
    return parser.parse_args()


def print_results(query: str, results) -> None:
    print(f"\nQuery: {query}")
    print("=" * 80)
    for result in results:
        print(f"#{result.rank} | score={result.score:.4f}")
        print(f"File: {result.path}")
        print(f"Preview: {result.preview}")
        print("-" * 80)


def main() -> None:
    args = parse_args()
    config = SearchEngineConfig(data_dir=args.data, top_k=args.top_k)
    engine = SearchEngine(config=config, strategy=create_strategy(args.strategy))
    engine.build_index()

    if args.query:
        print_results(args.query, engine.search(args.query))
        return

    print("Mini Search Engine. Type 'exit' to stop.")
    while True:
        query = input("\nSearch query: ").strip()
        if query.lower() in {"exit", "quit", "q"}:
            break
        if not query:
            print("Please enter a non-empty query.")
            continue
        print_results(query, engine.search(query))


if __name__ == "__main__":
    main()
