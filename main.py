from collections import Counter

def get_book_text(novel):
    with open(novel) as book:
        return book.read()

def word_count(subject: str) -> int:
     return len(subject.split())
     
def count_char(full_text):
    duplicates = {}
    for i in full_text:
        low = i.lower()
        if low in duplicates:
            duplicates[low] += 1
        else:
            duplicates[low] = 1
    return duplicates

def print_out_count(num_letter):
    for key, value in num_letter.items():
        if key.isalpha() == True:
            print(f"The '{key}' character was found {value} times")

def main():
    path_to_book: str ="books/frankenstein.txt"
    full_text = get_book_text(path_to_book)
    num_words: int = word_count(full_text)
    num_letter: dict = count_char(full_text)
    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{num_words} words found in the book.\n")
    print_out_count(num_letter)
    print("--- End report ---")

main()