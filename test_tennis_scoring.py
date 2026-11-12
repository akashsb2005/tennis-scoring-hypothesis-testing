
from hypothesis import given, strategies as st
import pytest

from tennis_scoring import parse_score, game_lead, set_spread


# Test 1: parse_score with valid inputs
@given(
    a=st.integers(min_value=0, max_value=1000),
    b=st.integers(min_value=0, max_value=1000)
)
def test_parse_score_valid(a, b):
    assert parse_score(f"{a}-{b}") == (a, b)


# Test 2: parse_score rejects invalid inputs
@pytest.mark.parametrize("value", ["", "-", "abc", "1-2-3", "-1-2"])
def test_parse_score_invalid(value):
    with pytest.raises(ValueError):
        parse_score(value)


# Test 3: game_lead with valid tennis scores
@given(
    first=st.sampled_from(["0", "15", "30", "40"]),
    second=st.sampled_from(["0", "15", "30", "40"])
)
def test_game_lead_valid(first, second):
    points = {"0": 0, "15": 1, "30": 2, "40": 3}
    assert game_lead(f"{first}-{second}") == (
        points[first] - points[second]
    )


# Test 4: game_lead rejects invalid inputs
@pytest.mark.parametrize("value", ["", "-", "abc", "50-40", "15-60"])
def test_game_lead_invalid(value):
    with pytest.raises(ValueError):
        game_lead(value)


# Test 5: set_spread with valid inputs
@given(st.lists(st.integers(min_value=0, max_value=1000), min_size=1))
def test_set_spread_valid(games):
    csv_input = ",".join(map(str, games))
    assert set_spread(csv_input) == max(games) - min(games)


# Test 6: set_spread rejects invalid inputs
@pytest.mark.parametrize("value", ["", "abc", "1,x,3", "-1,2"])
def test_set_spread_invalid(value):
    with pytest.raises(ValueError):
        set_spread(value)
