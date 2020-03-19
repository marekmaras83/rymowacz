import pytest

from rymowacz.rymowacz import get_rhyme_harmony, get_single_tone_rhyme_harmony


@pytest.mark.parametrize("input_word, expected_single_harmony, expected_harmony", [
    ("buba", ("a", 3), "uba"), ("wnet", ("et", 2), "et"), ('źrebak', ("ak", 4), "ebak"),
    ("wiem", ("iem", 1), "iem"), ('wieczór', ("ór", 5), "ieczór"),
    ("wij", ("ij", 1), "ij"), ("smutnie", ("ie", 5), "utnie"),
    ("to", ("o", 1), "o"),
    ("boa", ("a", 2), "oa"), ("zoo", ("o", 2), "oo"),
    ("kozi", ("i", 3), "ozi"), ("mi", ("i", 1), "i"),
    ("dziewczynka", ("a", 10), "ynka"),
    ("jojo", ("o", 3), "ojo"), ("jaja", ("ja", 2), "jaja"), ('zjem', ("jem", 1), "jem"),
    ("wdsfdsfhfgh", ("", 11), "")
])
def test_get_rhyme_harmony(input_word, expected_single_harmony, expected_harmony):

    assert get_single_tone_rhyme_harmony(input_word) == expected_single_harmony

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
