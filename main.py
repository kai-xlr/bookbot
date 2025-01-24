from collections import Counter

def main():
    book_path: str ="books/frankenstein.txt"
    full_text: list[str] = get_book_text(book_path)
    num_words: int = word_count(full_text)
    num_letter = count_char(full_text)
    print(f"{num_words} words found in the book.")
    print(f"Number of occurences of each letter in this book \n {num_letter}r")
    
def word_count(subject: list[str]) -> int:
    word_list = len(subject.split())
    return word_list

def get_book_text(path: list[str]) -> list[str]:
    with open(path) as book:
        return book.read()

def count_char(full_text):
    lowered_text = full_text.lower()
    char_count = Counter(lowered_text)
    duplicates = {char: count for char, count in char_count.items() if count > 1}
    return duplicates
main()