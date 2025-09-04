import sys
from stats import get_book_words, get_letter_count, sort_on
if len(sys.argv) == 2:
    book_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


#def main():
#    count = get_book_words("/Users/jacobbutz/workspace/github.com/bookbot/books/frankenstein.txt")
#    dictionary = get_letter_count("/Users/jacobbutz/workspace/github.com/bookbot/books/frankenstein.txt")
#    print(f"{count} words found in the document")
#    print (dictionary)

def main():
    count = get_book_words(book_path)
    dictionary = get_letter_count(book_path)
    sorted_letters = sorted(dictionary.items(), reverse = True, key = sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, freq in sorted_letters:
        print(f"{char}: {freq}")
    print("============= END ===============")
main()