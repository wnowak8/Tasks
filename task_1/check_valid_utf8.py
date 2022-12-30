
def check_valid_utf8(data):
    bytes_data = bytes(data)
    try:
        data=bytes_data.decode('utf8')
        return True, data
    except UnicodeError:
        return False
