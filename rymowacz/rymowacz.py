#! /usr/bin/python3

VOVELS = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
SOFTENING_PAIRS = {
    'i': VOVELS,
    'j': ['e', 'a'],
}


def is_multiple_vovel_syllable(word: str, i: int):
    for softening_prefix, possible_suffixes in SOFTENING_PAIRS.items():
        if word[i] == softening_prefix and word[i + 1] in possible_suffixes:
            return True
    return False


def has_one_syllable(word: str) -> bool:
    first_syllable_found = False
    word_length = len(word)

    letter_index = 0
    while letter_index < word_length:
        if word[letter_index] in VOVELS:
            if first_syllable_found:
                return False
            else:
                first_syllable_found = True
                if letter_index < len(word)-1 and is_multiple_vovel_syllable(word, letter_index):
                    letter_index += 1
        letter_index += 1

    return first_syllable_found


def find_simple_rhyme_core(word: str) -> int:
    reverse_enumerated_word = [(i, letter) for i, letter in enumerate(word)]
    reverse_enumerated_word.reverse()

    for letter_index, letter in reverse_enumerated_word:
        if letter in VOVELS:
            if letter_index != 0 and is_multiple_vovel_syllable(word, letter_index-1):
                return letter_index-1
            else:
                return letter_index


def get_rhyme_core(word: str) -> str:
    first_core_index = find_simple_rhyme_core(word)
    if has_one_syllable(word):
        return word[first_core_index::]
    else:
        standard_rhyme_index = find_simple_rhyme_core(word[:first_core_index])
        return word[standard_rhyme_index::]


if __name__ == "__main__":
    while True:
        word = input("Enter word to rhyme: ")
        print(f"rhyme core for word {word} is {get_rhyme_core(word)}")
