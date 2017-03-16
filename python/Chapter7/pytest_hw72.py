import pytest

from hw72_using_with import calculateSum

test_data = [
    ("C:\Users\watts\Documents\GitHub\python\mbox-short.txt",0.7507185185185187),
    ("C:\Users\watts\Documents\GitHub\python\word.txt",0),
]

@pytest.mark.parametrize("file_name,expected", test_data, ids=["Average mbox-short.txt", "Average word.txt"])
def test_calculateSum(file_name,expected):
    average = calculateSum(file_name)
    assert average == expected