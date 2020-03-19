#! /usr/bin/python3

VOVELS = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
CENTRALIZED_DIPHTHONGS = {
    'i': VOVELS,
    'j': ['e', 'a'],
}


def is_centralized_diphthong(word_to_check: str, letter_index: int):
    for prefix, possible_suffixes in CENTRALIZED_DIPHTHONGS.items():
        if word_to_check[letter_index] == prefix and word_to_check[letter_index + 1] in possible_suffixes:
            return True
    return False


def has_one_syllable(word: str) -> bool:
    first_harmony_found = False
    word_length = len(word)

    letter_index = 0
    while letter_index < word_length:
        if word[letter_index] in VOVELS:
            if first_harmony_found:
                return False
            else:
                first_harmony_found = True
                if letter_index < len(word)-1 and is_centralized_diphthong(word, letter_index):
                    letter_index += 1
        letter_index += 1

    return first_harmony_found


def find_single_tone_rhyme_harmony(word: str) -> int:
    reverse_enumerated_word = [(i, letter) for i, letter in enumerate(word)]
    reverse_enumerated_word.reverse()

    for letter_index, letter in reverse_enumerated_word:
        if letter in VOVELS:
            if letter_index != 0 and is_centralized_diphthong(word, letter_index - 1):
                return letter_index-1
            else:
                return letter_index


def get_rhyme_harmony(word: str) -> str:
    first_core_index = find_single_tone_rhyme_harmony(word)
    if has_one_syllable(word):
        return word[first_core_index::]
    else:
        standard_rhyme_index = find_single_tone_rhyme_harmony(word[:first_core_index])
        return word[standard_rhyme_index::]


if __name__ == "__main__":
    while True:
        word = input("Enter word to rhyme: ")
        print(f"rhyme harmony for word '{word}' is '{get_rhyme_harmony(word)}'")
