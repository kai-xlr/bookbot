def main():
    book_path: str ="books/frankenstein.txt"
    full_text: list[str] = get_book_text(book_path)
    num_words: list[str] = word_count(full_text)
    print(f"{num_words} words found in the book.")
    
def word_count(subject: list[str]) -> list[str]:
    word_list = len(subject.split())
    return word_list

def get_book_text(path: list[str]) -> list[str]:
    with open(path) as book:
        return book.read()

main()