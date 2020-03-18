VOVELS = ['a', 'ą', 'e', 'ę', 'i', 'j', 'o', 'ó', 'u']
SOFTENING_VOVEL = 'i'
MULTI_VOVEL_SYLLABLE_PREFIXES = ['j', SOFTENING_VOVEL]


def has_one_syllable(word: str):
    first_syllable_found = False
    word_length = len(word)

    i = 0
    while i < word_length:
        if word[i] in VOVELS:
            if first_syllable_found:
                return False
            else:
                first_syllable_found = True
                if is_multiple_vovel_syllable(word, i):
                    i += 1
        i += 1

    return first_syllable_found


def is_multiple_vovel_syllable(word, i):
    return word[i] in MULTI_VOVEL_SYLLABLE_PREFIXES and word[i+1] in VOVELS


def get_last_syllable(word: str):
    word = word.lower()
    # for i in range(len(word)):

    pass
