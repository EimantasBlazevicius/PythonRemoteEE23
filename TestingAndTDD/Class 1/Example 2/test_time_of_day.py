import time_of_day


def test_what_time():
    morning = 6
    day = 11
    evening = 19
    night = 23
    assert time_of_day.what_time(morning) == "Morning"
    assert time_of_day.what_time(day) == "Day"
    assert time_of_day.what_time(evening) == "Evening"
    assert time_of_day.what_time(night) == "Night"
