def int_to_bin(int_data: list):
    """Convert data from integer to binary.
    Args:
        int_data (list): List of integer data.
    Returns:
        bin_data (list): List of converted data to binary.
    """

    bin_data=[]
    for j in range(len(int_data)):
        bin_data.insert(j,bin(int_data[j]).replace("0b",""))
        if len(bin_data[j]) < 8:
            bin_data[j]=(8-len(bin_data[j]))*'0'+bin_data[j]
    return bin_data


def check_valid_utf8(int_data:list):
    """Check if byte after continuation byte is valid.
    Args:
        int_data (list): List of integer data.
    Returns:
        is_valid (bool): Result of data validation.
    """

    bin_data=int_to_bin(int_data)
    for i in range(len(bin_data)):
        if bin_data[i].startswith('11110'):
            if i >= len(bin_data)-3 or not (bin_data[i+1].startswith('10') and bin_data[i+2].startswith('10') and bin_data[i+3].startswith('10')): 
                is_valid=False
                break
        if bin_data[i].startswith('1110'):
            if i >= len(bin_data)-2 or not (bin_data[i+1].startswith('10') and bin_data[i+2].startswith('10')):
                is_valid=False
                break
        if bin_data[i].startswith('110'):
            if i >= len(bin_data)-1 or not bin_data[i+1].startswith('10'):
                is_valid=False
                break
        else:
            is_valid=True
    return is_valid
