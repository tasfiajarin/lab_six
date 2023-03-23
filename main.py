def encode(lock_code):
    encoded = ''  # empty string to add units later on
    for x in lock_code:
        num = int(x) + 3
        encoded += str(num)
    return encoded


def decode(encoded):
    decoded = ""
    for x in encoded:
	    x = int(x)
	    x -+ 3
	    x = str(x)
	    decoded += x
    return decoded



def main():
    encoded = None
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()

        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            lock_code = input('Please enter your password to encode: ')
            encoded = encode(lock_code)
            print('Your password has been encoded and stored.')
        elif menu_option == 2:
            decoded = decode(encoded)  #calls parter's function and saves it
            print('The encoded password is ' + encoded + 'and the original password is ' + decoded + '.')
        elif menu_option == 3:
            break


if __name__ == '__main__':
    main()
