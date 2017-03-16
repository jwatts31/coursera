import pytest

from hw85_using_with import findEmailsFrom

test_data = [
    ("C:\Users\watts\Documents\GitHub\python\mbox-short.txt","C:\Users\watts\Documents\GitHub\python\emails.txt"),
]

@pytest.mark.parametrize("file_name,expected_file_emails", test_data, ids=["Emails from mbox-short.txt"])
def test_calculateSum(file_name,expected_file_emails):
    actual_emails = findEmailsFrom(file_name)
    
    with open(expected_file_emails,'r') as file_handler:
        expected_emails = []
        for line in file_handler:
            line = line.rstrip()
            expected_emails.append(line)

        assert expected_emails == actual_emails