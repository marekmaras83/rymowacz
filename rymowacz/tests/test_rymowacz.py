import pytest

from rymowacz.rymowacz import has_one_syllable, get_rhyme_harmony, find_single_tone_rhyme_harmony


@pytest.mark.parametrize("input_word, expected_size_check, expected_simple_core, expected_core", [
    ("buba", False, "a", "uba"), ("wnet", True, "et", "et"), ('źrebak', False, "ak", "ebak"),
    ("wiem", True, "iem", "iem"), ('wieczór', False, "ór", "ieczór"),
    ("wij", True, "ij", "ij"), ("smutnie", False, "ie", "utnie"),
    ("to", True, "o", "o"),
    ("boa", False, "a", "oa"), ("zoo", False, "o", "oo"),
    ("kozi", False, "i", "ozi"), ("mi", True, "i", "i"),
    ("dziewczynka", False, "a", "ynka"),
    ("jojo", False, "o", "ojo"), ("jaja", False, "ja", "jaja"), ('zjem', True, "jem", "jem"),
])
def test_get_rhyme_harmony(input_word, expected_size_check, expected_simple_core, expected_core):
    assert has_one_syllable(input_word) is expected_size_check
    assert input_word[find_single_tone_rhyme_harmony(input_word)::] == expected_simple_core
    assert get_rhyme_harmony(input_word) == expected_core


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
