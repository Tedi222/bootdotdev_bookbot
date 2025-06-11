from stats import get_num_words, get_character_count

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    
    return book_contents

if __name__ == "__main__":
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    characters = get_character_count(book)
    print(f"{num_words} words found in the document")
    print(characters)