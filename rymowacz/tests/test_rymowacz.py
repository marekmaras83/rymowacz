import pytest

from rymowacz.rymowacz import get_rhyme_harmony, find_single_tone_rhyme_harmony


@pytest.mark.parametrize("input_word, expected_single_harmony, expected_harmony", [
    ("buba", "a", "uba"), ("wnet", "et", "et"), ('źrebak', "ak", "ebak"),
    ("wiem", "iem", "iem"), ('wieczór', "ór", "ieczór"),
    ("wij", "ij", "ij"), ("smutnie", "ie", "utnie"),
    ("to", "o", "o"),
    ("boa", "a", "oa"), ("zoo", "o", "oo"),
    ("kozi", "i", "ozi"), ("mi", "i", "i"),
    ("dziewczynka", "a", "ynka"),
    ("jojo", "o", "ojo"), ("jaja", "ja", "jaja"), ('zjem', "jem", "jem"),
    ("wdsfdsfhfgh", "", "")
])
def test_get_rhyme_harmony(input_word, expected_single_harmony, expected_harmony):

    found_harmony_index = find_single_tone_rhyme_harmony(input_word)
    assert input_word[found_harmony_index::] == expected_single_harmony

    assert get_rhyme_harmony(input_word) == expected_harmony


# ====== niedokładne:
# y/i
# spływa
# oliwa.

# y/i
# zipie,
# sypie.

# y/i
# świnie,
# skrzynie.
