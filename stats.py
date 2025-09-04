def get_book_words(book_path):
    with open(book_path, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
    return word_count

def get_letter_count(book_path):
    with open(book_path, 'r') as file:
        content = file.read()
        content = content.lower() # Normalize to lowercase
        dictionary = {}
        for char in content:
            if char.isspace():
                continue  # Skip spaces and all whitespace
            dictionary[char] = dictionary.get(char, 0) + 1
    return dictionary

def sort_on(item):
    return item[1]