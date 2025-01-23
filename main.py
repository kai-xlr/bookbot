def main():
    book_path: str ="books/frankenstein.txt"
    full_text: list[str] = get_book_text(book_path)
    num_words: list[str] = word_count(full_text)
    print(f"{num_words} words found in the book.")
    
def word_count(subject: list[str]) -> list[str]:
    wordlist = len(subject.split())
    return wordlist

def get_book_text(path: list[str]) -> list[str]:
    with open(path) as book:
        return book.read()

main()