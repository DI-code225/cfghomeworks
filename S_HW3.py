def generate_phrase(characters, phrase):
    characters_list = list(characters)
    phrase_list = list(phrase)
    new_phrase = []
    returns_true = 0

    for x in range(len(phrase_list)):
        if phrase_list[x].isupper():
            new_phrase += phrase_list[x].lower()
        else:
            new_phrase += phrase_list[x]

    length = len(new_phrase)
    for y in range(length):

        if new_phrase[y] in characters_list:
            characters_list.remove(new_phrase[y])
            returns_true = returns_true + 1
        else:
            return False

    if returns_true == length:
        return True
    else:
        return False




# example:True
print(generate_phrase('cpolasaype', 'Apocalypse'))



