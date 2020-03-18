import pytest

from rymowacz.rymowacz import has_one_syllable, get_standard_rhyme_core, find_simple_rhyme_core


@pytest.mark.parametrize("input_word, output", [
    ("buba", False), ("wnet", True), ('źrebak', False),
    ("wiem", True), ('zjem', True), ('wieczór', False),
    ("to", True),
    ("boa", False),
])
def test_count_syllables(input_word, output):
    assert has_one_syllable(input_word) is output


@pytest.mark.parametrize("input_word, expected_output", [
    ("wnet", "et"),
    ("wiem", "iem"), ('zjem', "jem"),
    ("to", "o"),
    ("zło", "o"),
    ("zoo", "o")
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

