def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_words(text)
    chars_dict = get_character_appearances(text)
    print(chars_dict)

def get_character_appearances(text):
    lower_text = text.lower()
    characters = {}
    for s in text:
        character = s
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_words(book):
    words = book.split()
    return len(words)

main()