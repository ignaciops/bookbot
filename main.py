def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_words(text)
    chars_dict = get_character_appearances(text)
    get_report(book_path, num_words, chars_dict)
    

def get_character_appearances(text):
    lower_text = text.lower()
    characters = {}
    for s in lower_text:
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

def get_report(book_path, word_count, char_dict):
    # Data preparation
    header = f"--- Begin report of {book_path} ---"
    count = f"{word_count} words found in the document"
    letters = {key: value for key, value in char_dict.items() if key.isalpha()}
    letters_list = [{"char": char, "num": num} for char, num in letters.items()]
    
    # Helper function
    def sort_on(dict):
        return dict["num"]
    
    # Processing data
    letters_list.sort(reverse=True, key=sort_on)
    
    # Output
    print(header)
    print(count)
    for letter in letters_list:
        char = letter["char"]
        num = letter["num"]
        print(f"The '{char}' character was found {num} times")
    print("--- End report ---")


main()