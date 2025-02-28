"""Bookbot Project."""

import sys
from stats import print_report


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(f"{book_path}") as book:
        book = book.read()
    print(print_report(book, book_path))


if __name__ == "__main__":
    main()
