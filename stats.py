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

def sort_on(dict):
    return dict['count']

def to_list(char_dict):
    ls_char = []
    for char in char_dict:
        if char.isalpha():
            ls_char.append({'character': char, 'count': char_dict[char]})
    ls_char.sort(reverse=True, key=sort_on)
    return ls_char