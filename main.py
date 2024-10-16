def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_chars(text):
    char_dict = {}
    for word in text:
        lowered_word = word.lower()
        if lowered_word in char_dict:
            char_dict[lowered_word] +=1
        else:
            char_dict[lowered_word] = 1
    return char_dict

book_path = "books/frankenstein.txt"

text = get_book_text(book_path)

num_words = get_num_words(text)

chars_num = get_num_chars(text)

print(f"{num_words} words found in the document")

print(chars_num)