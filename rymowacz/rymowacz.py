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


def get_single_tone_rhyme_harmony(word: str) -> (str, int):
    reverse_enumerated_word = [(i, letter) for i, letter in enumerate(word)]
    reverse_enumerated_word.reverse()

    for letter_index, letter in reverse_enumerated_word:
        if letter in VOVELS:
            if letter_index != 0 and is_centralized_diphthong(word, letter_index - 1):
                return word[letter_index-1:], letter_index-1
            else:
                return word[letter_index:], letter_index
    return '', len(word)


def get_rhyme_harmony(word: str) -> str:
    harmony = ''
    previous_harmony_letter_index = len(word)

    for harmony_id in range(2):
        single_harmony, harmony_index = get_single_tone_rhyme_harmony(word[:previous_harmony_letter_index])
        harmony = single_harmony + harmony
        previous_harmony_letter_index = harmony_index

    return harmony


if __name__ == "__main__":
    while True:
        word = input("Enter word to rhyme: ")
        print(f"rhyme harmony for word '{word}' is '{get_rhyme_harmony(word)}'")
