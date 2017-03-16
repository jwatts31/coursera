import pytest

import hw13_2_for_pytest

test_data = [
    ("http://python-data.dr-chuck.net/comments_42.json", 2553),
    ("http://python-data.dr-chuck.net/comments_350839.json", 2423),
    ("http://google.com", None),
]

@pytest.mark.parametrize("addresss,expected_return", test_data, ids=["Url 1 Valid","Url 2 Valid", "Url 3 Invalid"])
def test_parse_comment_counts(addresss,expected_return):
    actual_return = hw13_2_for_pytest.parse_comment_counts(addresss)
   
    assert  actual_return == expected_return