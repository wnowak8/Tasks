
def check_valid_utf8(data):
    bytes_data = bytes(data)
    #print(bytes_data)
    try:
        data=bytes_data.decode('utf8')
        return True, data
    except UnicodeError:
        return False
d,a=check_valid_utf8(data = [ 110, 101, 114, 32, 198, 138, 101, 118, 101, 108, 111, 112, 109, 101, 110, 116]
)
print(a)
# print(f'{data_2=}')
# print(f'{is_valid=}')