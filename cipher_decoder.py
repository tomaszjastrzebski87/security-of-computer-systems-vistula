def binary_read_file(filename: str):
    with open(filename, 'rb') as file_to_read:
        binary_file_contents: bytes = file_to_read.read()
    return binary_file_contents


def convert_binaries_to_decimals(binaries_to_convert: bytes):
    decimals_list: list[int] = [int(byte) for byte in binaries_to_convert]
    return decimals_list


def decode_cipher(list_of_codes: list[int]):
    decoded_cipher: list = []
    for code in list_of_codes:
        decoded_sign = digits_to_letters[code]
        decoded_cipher.append(decoded_sign)
    decoded_text: str = ''.join(decoded_cipher)
    return decoded_text


digits_to_letters: dict = {
    0: 'A',
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'I',
    17: 'N',
    18: 'M',
    19: 'Ł',
    20: 'L',
    21: 'K',
    22: 'J',
    23: 'I',
    24: 'H',
    25: 'G',
    26: 'F',
    27: 'T',
    28: 'U',
    29: 'W',
    30: 'Z',
    31: 'Y',
    32: 'Ż',
    33: 'Ż',
    34: ' ',
}


def main():
    code_to_decipher_bytes: bytes = binary_read_file("przeciek.bin")
    bytes_converted_to_decimals: list[int] = convert_binaries_to_decimals(code_to_decipher_bytes)
    decoded_cipher: str = decode_cipher(bytes_converted_to_decimals)
    print(decoded_cipher)


if __name__ == '__main__':
    main()
