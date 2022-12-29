from calculate_damages import calculate_damage


def test():
    assert calculate_damage('fire','grass') == '2x'
    assert calculate_damage('fighting','ice rock') == '4x'
    assert calculate_damage('psychic','poison dark') == '0x'
    assert calculate_damage('water','normal') == '1x'
    assert calculate_damage('fire','rock') == '0.5x'

if __name__ == "__main__":
    test()
    print("Everything passed")