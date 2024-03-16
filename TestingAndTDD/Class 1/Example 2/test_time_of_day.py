import pytest

import time_of_day


@pytest.mark.parametrize("time, label", [(6, "Morning"), (11, "Day"), (19, "Evening"), (23, "Night"), (4, "Night")])
def test_what_time(time, label):
    assert time_of_day.what_time(time) == label
