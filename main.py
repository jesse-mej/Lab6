#  Jesse Mejia

def encode(password):
    final_password = "" # string to be concatenated
    for num in password: # go through each digit
        shifted_num = (int(num) + 3) # add 3 to digit
        corrected_num = shifted_num%10  # for numbers like 7,8,9 mod 10 will shift it correctly up i.e. 12 becomes 2
        final_password += str(corrected_num)
    return final_password

def decode(final_password):
    new_pass = ""
    for x in final_password:
        shifted_num = int(x) - 3 # subtracts 3
        new_shift = shifted_num % 10 # correctly shifts numbers that will add to greater than 10
        new_pass += str(new_shift) # adds to string
    print('The encoded password is', final_password, ',and the original password is', new_pass, '.')


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        selection = input("Please enter an option: ")

        if selection == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()

        elif selection == '2':
            decode(encode(password))

        elif selection == '3':
            break


if __name__ == "__main__":
    main()
