import pytest

from rymowacz.rymowacz import has_one_syllable, get_last_syllable, get_simple_rhyme_core, get_standard_rhyme_core, \
    find_simple_rhyme_core


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
])
def test_get_simple_rhyme_core(input_word, expected_output):
    assert get_simple_rhyme_core(input_word) == expected_output


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
    ('wieczór', "ieczór"),
    ("boa", "oa"),
])
def test_get_standard_rhyme_core(input_word, output):
    assert get_standard_rhyme_core(input_word) == output


# @pytest.mark.parametrize("input_word, output", [
#     ("buba", "ba"),
# ])
# def test_get_last_syllable(input_word, output):
#     assert get_last_syllable(input_word) == output


# rhymes
# kura - góra # ten sam dźwięk, inna pisownia
#
# wyraz 1 sylabowy: rym do jednej sylaby (rym męski)
# kot-let : sza-let # słaby rym

#
# wo-dy - och-ło-dy

# ====== dokładne:
# ---------- rymy żeńskie
# y-wa
# lokomotywa,
# spływa:

# u-cha
# dmucha,
# bucha:

# o-nie, różna ilość sylab
# wagonie,
# konie,

# a-nów
# bananów,
# fortepianów,

# ie-ści
# czterdzieści,
# mieści.

# le-tów
# atletów
# kotletów,

# inna pisownia, zmiękczenie
# smutnie:
# kłótnie,
#
# Po co wasze swary głupie,
# Wnet i tak zginiemy w zupie!"

# -------- rymy męskie
# -a
# gna
# pcha

# -jem/-iem
# wiem
# zjem

# -ost
# wprost!
# most,

# -as
# las,
# czas,

# -as
# dal,
# stal,

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

