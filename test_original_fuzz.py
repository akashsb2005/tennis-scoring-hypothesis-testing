
from hypothesis import given, strategies as st

from tennis_scoring_original import (
    parse_score,
    game_lead,
    set_spread
)


@given(st.one_of(st.text(), st.none()))
def test_parse_score_no_crash(s):
    try:
        parse_score(s)
    except Exception as e:
        assert False, f"parse_score crashed with {s!r}: {e}"


@given(st.one_of(st.text(), st.none()))
def test_game_lead_no_crash(s):
    try:
        game_lead(s)
    except Exception as e:
        assert False, f"game_lead crashed with {s!r}: {e}"


@given(st.one_of(st.text(), st.none()))
def test_set_spread_no_crash(s):
    try:
        set_spread(s)
    except Exception as e:
        assert False, f"set_spread crashed with {s!r}: {e}"
