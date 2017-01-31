import pytest

from hw46_one_function import computepay

test_data = [
    (40,11.25,450),
    (35,15,525),
    (50.5,12.25,682.94),
    (45.5,25.5,1230.38),
    (40.25,16,646.0),
    (45.50,17.50,844.38),
]

@pytest.mark.parametrize("hours,work,expected", test_data)
def test_computepay(hours,work, expected):
    total_pay = computepay(hours,work)
    assert total_pay == expected