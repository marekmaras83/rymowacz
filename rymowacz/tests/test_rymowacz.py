import pytest

from rymowacz.rymowacz import has_one_syllable, get_standard_rhyme_core, find_simple_rhyme_core


@pytest.mark.parametrize("input_word, expected_output", [
    ("buba", False), ("wnet", True), ('źrebak', False),
    ("wiem", True), ('zjem', True), ('wieczór', False), ("wij", True),
    ("to", True),
    ("boa", False), ("zoo", False),
    ("kozi", False), ("mi", True)
])
def test_has_one_syllable(input_word, expected_output):
    assert has_one_syllable(input_word) is expected_output


@pytest.mark.parametrize("input_word, expected_output", [
    ("buba", "a"), ("wnet", "et"), ('źrebak', "ak"),
    ("wiem", "iem"), ('zjem', "jem"), ('wieczór', "ór"), ("wij", "ij"),
    ("to", "o"),
    ("boa", "a"), ("zoo", "o"),
    ("kozi", "i"), ("mi", "i")
])
def test_find_simple_rhyme_core(input_word, expected_output):
    assert input_word[find_simple_rhyme_core(input_word)::] == expected_output


@pytest.mark.parametrize("input_word, output", [
    ("buba", "uba"), ('źrebak', "ebak"),
    ('wieczór', "ieczór"), ("smutnie", "utnie"),
    ("boa", "oa"),
])
def test_get_standard_rhyme_core(input_word, output):
    assert get_standard_rhyme_core(input_word) == output


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

