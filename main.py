"""Bookbot Project."""


def count_words(book_string: str) -> int:
    count = len(book_string.split())
    return count


def count_chars(book_string: str) -> dict[str, int]:
    chars = set(
        [char.lower() for word in book_string for char in word if char.isalpha()]
    )
    chars_count = {char: book_string.lower().count(char) for char in chars}
    return chars_count


def print_report(book_string: str) -> str:
    words_count = count_words(book_string)
    chars_count = count_chars(book_string)
    begin_line = "--- Begin report of books/frankenstein.txt ---"
    end_line = "--- End report ---"
    words_line = f"{words_count} words found in the document"
    chars_lines = ""
    for char, count in chars_count.items():
        chars_lines += f"The '{char}' character was found {count} times"
        chars_lines += "\n"
    return f"{begin_line}\n{words_line}\n\n{chars_lines}{end_line}"


if __name__ == "__main__":
    with open("books/frankenstein.txt") as book:
        book = book.read()

    print(count_words(book))
    print(count_chars(book))
    print(print_report(book))
