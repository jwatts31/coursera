import pytest

import hw13_3_pytest

test_data = [
    ("University of West Florida", "ChIJWWcAJ8nAwogRKfVGTRp9CNk"),
    ("IT College of Estonia", "ChIJtwfNmKmVkkYRytROXZXtFbM"),
    ("Kyiv Unisersity of Oriental Language", "ChIJBUVa4U7P1EAR_kYBF9IxSXY"),
    ("BITS Pilani", "ChIJiS2H9mQZEzkR_Vg0F3qaGsM"),
    ("City of Westminster College", "ChIJ5ayEXDebRoYRRBOEyYdHstM"),
    ("University of Texas at Austin", "ChIJZe22kZq1RIYR4Ed2g630JxE"),
    ("Texas",None),
]

@pytest.mark.parametrize("addresss,expected_return", test_data, ids=["Location Florida Valid","Location Estonia Valid", "Location Kyiv Valid", "Location BITS Valid", "Location Westminster Valid","Location Texas at Austin Valid", "Location Invalid"])
def test_find_location(addresss,expected_return):
    actual_return = hw13_3_pytest.find_location(addresss)
   
    assert  actual_return == expected_return