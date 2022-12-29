from check_valid_utf8 import check_valid_utf8

valid_1 = [225, 143, 169, 114, 111, 115, 110, 101, 114, 32, 198, 138, 101, 118, 101, 108, 111, 112, 109, 101, 110, 116]
valid_2 = [71, 114, 111, 115, 110, 101, 114, 32, 68, 101, 118, 101, 108, 111, 112, 109, 101, 110, 116]
valid_3 = [76, 117, 98, 105, 196, 153, 32, 240, 159, 140, 173]

invalid_1 = [225, 143, 41, 114, 111, 115, 110, 101, 114, 32, 198, 138, 101, 118, 101, 108, 111, 112, 109, 101, 110, 116]
invalid_2 = [225, 143, 169, 114, 111, 115, 110, 101, 114, 32, 198, 202, 101, 118, 101, 108, 111, 112, 109, 101, 110, 116]
invalid_3 = [76, 117, 98, 105, 196, 153, 32, 240, 159, 140, 109]
invalid_4 = [76, 117, 98, 105, 196, 89, 32, 240, 159, 140, 173]


def test():
    assert check_valid_utf8(valid_1) == True
    assert check_valid_utf8(valid_2) == True
    assert check_valid_utf8(valid_3) == True

    assert check_valid_utf8(invalid_1) == False
    assert check_valid_utf8(invalid_2) == False
    assert check_valid_utf8(invalid_3) == False
    assert check_valid_utf8(invalid_4) == False


if __name__ == "__main__":
    test()
    print("Everything passed")