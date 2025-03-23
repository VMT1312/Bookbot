from stats import *
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)

    num_words = get_num_words(text)

    chars_num = get_num_chars(text)

    ls_chars_num = to_list(chars_num)

    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{num_words} words found in the document")

    for i in range(len(ls_chars_num)):
        character = ls_chars_num[i]['character']
        times = ls_chars_num[i]['count']
        print(f"{character}: {times}")

    print("--- End report ---")

main()