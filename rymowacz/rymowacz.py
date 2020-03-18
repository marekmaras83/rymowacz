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


def find_simple_rhyme_core(word: str) -> int:
    reverse_enumerated_word = [(i, letter) for i, letter in enumerate(word)]
    reverse_enumerated_word.reverse()

    for index, letter in reverse_enumerated_word:
        if letter in VOVELS:
            if index != 0 and word[index-1] in MULTI_VOVEL_SYLLABLE_PREFIXES:
                return index-1
            else:
                return index


def get_standard_rhyme_core(word):
    first_core_index = find_simple_rhyme_core(word)
    standard_rhyme_index = find_simple_rhyme_core(word[:first_core_index])
    return word[standard_rhyme_index::]


def get_last_syllable(word: str):
    word = word.lower()
    # for i in range(len(word)):

    pass
