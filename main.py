def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    
    return book_contents

def get_words_num(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_words_num(book)
    print(f"{num_words} words found in the document")