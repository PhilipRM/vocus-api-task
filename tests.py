from api import is_valid_number

def number_too_long():
    assert (not is_valid_number("1550705666276441"))

def number_too_short():
    assert (not is_valid_number("1"))
    assert (not is_valid_number("12"))
    assert (not is_valid_number("123"))
    assert (not is_valid_number("1234"))
    assert (not is_valid_number("12345"))
    assert (not is_valid_number("123456"))
    assert (not is_valid_number("1234567"))
    assert (not is_valid_number("12345678"))
    assert (not is_valid_number("123456789"))

def valid_phone_numbers():
    assert is_valid_number("14077454579")
    assert is_valid_number("93713653157")
    assert is_valid_number("35849463776")
    assert is_valid_number("355693908352")
    assert is_valid_number("213558613768")
    assert is_valid_number("16847825893")

if __name__ == "__main__":
    number_too_long()
    number_too_short()
    valid_phone_numbers()
    print("tests passed")
