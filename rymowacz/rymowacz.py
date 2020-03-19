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


def find_single_tone_rhyme_harmony(word: str) -> int:
    reverse_enumerated_word = [(i, letter) for i, letter in enumerate(word)]
    reverse_enumerated_word.reverse()

    for letter_index, letter in reverse_enumerated_word:
        if letter in VOVELS:
            if letter_index != 0 and is_centralized_diphthong(word, letter_index - 1):
                return letter_index-1
            else:
                return letter_index
    return len(word)


def get_rhyme_harmony(word: str) -> str:
    harmony = ''
    harmony_letter_index = len(word)
    previous_harmony_letter_index = harmony_letter_index

    for harmony_id in range(2):
        harmony_letter_index = find_single_tone_rhyme_harmony(word[:previous_harmony_letter_index])
        harmony = word[harmony_letter_index:previous_harmony_letter_index] + harmony
        previous_harmony_letter_index = harmony_letter_index

    return harmony


if __name__ == "__main__":
    while True:
        word = input("Enter word to rhyme: ")
        print(f"rhyme harmony for word '{word}' is '{get_rhyme_harmony(word)}'")
