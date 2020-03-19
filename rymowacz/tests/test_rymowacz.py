from functools import reduce

import pytest

from rymowacz.rymowacz import get_rhyme_harmony, get_single_tone_rhyme_harmony, get_rhymes


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


@pytest.fixture
def input_dictionary():
    rhymes_per_harmony = {
        "uba": ["buba", "podróba"],
        "et": ["wnet", "net"],
        "ebak": ["źrebak", "chlebak"],
        "iem": ["wiem", "ciem"],
        "ieczór": ["wieczór"],
    }
    return reduce(list.__add__, rhymes_per_harmony.values())


@pytest.mark.parametrize("input_harmony, expected_rhymes", [
    ("uba", ["buba", "podróba"]),
    ("et", ["wnet", "net"]), ("ebak", ['źrebak', "chlebak"]),
    # ("wiem", ("iem", 1), "iem"), ('wieczór', ("ór", 5), "ieczór"),
    # ("wij", ("ij", 1), "ij"), ("smutnie", ("ie", 5), "utnie"),
    # ("to", ("o", 1), "o"),
    # ("boa", ("a", 2), "oa"), ("zoo", ("o", 2), "oo"),
    # ("kozi", ("i", 3), "ozi"), ("mi", ("i", 1), "i"),
    # ("dziewczynka", ("a", 10), "ynka"),
    # ("jojo", ("o", 3), "ojo"), ("jaja", ("ja", 2), "jaja"), ('zjem', ("jem", 1), "jem"),
])
def test_get_rhymes(input_harmony, expected_rhymes, input_dictionary):
    assert get_rhymes(input_harmony, input_dictionary) == expected_rhymes

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
