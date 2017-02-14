import pytest

import hw94_for_pytest

test_data = [
    ("C:\Users\watts\Documents\GitHub\python\mbox-short.txt",{'cwen@iupui.edu': 5}),
]

@pytest.mark.parametrize("file_name,expected_return", test_data, ids=["Emails from mbox-short.txt"])
def test_countSenders(file_name,expected_return):
    actual_emails = hw94_for_pytest.get_senders(file_name)
    actual_return = hw94_for_pytest.count_senders(actual_emails)
   
    assert  actual_return == expected_return