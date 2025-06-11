from stats import get_num_words, get_character_count, sort_characters
import sys
def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    
    return book_contents

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    
    num_words = get_num_words(book)
    characters = get_character_count(book)
    counts = sort_characters(characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in counts:
        print(f"{i["character"]}: {i["num"]}")