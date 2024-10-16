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

def to_list(char_dict):
    ls_char = []
    c = {}
    for word in text:
        check = {}
        lowered = word.lower()
        if lowered.isalpha() and lowered not in c:
            c[lowered] = char_dict[lowered]
            check['character'] = lowered
            check['count'] = c[lowered]
            ls_char.append(check)
    return ls_char

book_path = "books/frankenstein.txt"

text = get_book_text(book_path)

num_words = get_num_words(text)

chars_num = get_num_chars(text)

ls_chars_num = to_list(chars_num)

print(f"{num_words} words found in the document")

print(ls_chars_num)