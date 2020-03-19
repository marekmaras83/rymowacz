import pytest

from rymowacz.rymowacz import has_one_syllable, get_rhyme_core, find_simple_rhyme_core


@pytest.mark.parametrize("input_word, expected_output", [
    ("buba", False), ("wnet", True), ('źrebak', False),
    ("wiem", True), ('zjem', True), ('wieczór', False), ("wij", True), ("smutnie", False),
    ("to", True),
    ("boa", False), ("zoo", False),
    ("kozi", False), ("mi", True)
])
def test_has_one_syllable(input_word, expected_output):
    assert has_one_syllable(input_word) is expected_output


@pytest.mark.parametrize("input_word, expected_output", [
    ("buba", "a"), ("wnet", "et"), ('źrebak', "ak"),
    ("wiem", "iem"), ('zjem', "jem"), ('wieczór', "ór"), ("wij", "ij"), ("smutnie", "ie"),
    ("to", "o"),
    ("boa", "a"), ("zoo", "o"),
    ("kozi", "i"), ("mi", "i")
])
def test_find_simple_rhyme_core(input_word, expected_output):
    assert input_word[find_simple_rhyme_core(input_word)::] == expected_output


@pytest.mark.parametrize("input_word, expected_output", [
    ("buba", "uba"), ("wnet", "et"), ('źrebak', "ebak"),
    ("wiem", "iem"), ('zjem', "jem"), ('wieczór', "ieczór"), ("wij", "ij"), ("smutnie", "utnie"),
    ("to", "o"),
    ("boa", "oa"), ("zoo", "oo"),
    ("kozi", "ozi"), ("mi", "i")
])
def test_get_rhyme_core(input_word, expected_output):
    assert get_rhyme_core(input_word) == expected_output


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
