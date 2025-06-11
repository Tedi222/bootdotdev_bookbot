def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    text = text.lower()
    characters_set = set(text)
    characters_dict = {}
    for c in characters_set:
        characters_dict[c] = text.count(c)
    return characters_dict