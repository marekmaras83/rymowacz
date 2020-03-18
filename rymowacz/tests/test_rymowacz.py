import pytest

from rymowacz.rymowacz import has_one_syllable, get_last_syllable


@pytest.mark.parametrize("input_word, output", [
    ("buba", False), ("wnet", True), ("wiem", True), ('zjem', True), ('źrebak', False), ('wieczór', False), ("to", True)
])
def test_count_syllables(input_word, output):
    assert has_one_syllable(input_word) is output


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

