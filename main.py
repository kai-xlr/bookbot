from collections import Counter

def main():
    path_to_book: str ="books/frankenstein.txt"
    full_text = get_book_text(path_to_book)
    num_words: int = word_count(full_text)
    num_letter: dict = count_char(full_text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the book.")
    print()
    print_out_count(num_letter)
    print("--- End report ---")
    
def word_count(subject: str) -> int:
    word_list = len(subject.split())
    return word_list

def get_book_text(novel):
    with open(novel) as book:
        return book.read()

def count_char(full_text):
    lowered_text = full_text.lower()
    cleaned_string = ''.join([i for i in lowered_text if i.isalpha()])
    char_count = Counter(cleaned_string)
    duplicates = {char: count for char, count in char_count.items() if count > 1}
    return duplicates

def print_out_count(num_letter):
    for key, value in num_letter.items():
        print(f"The '{key}' character was found {value} times")
main()