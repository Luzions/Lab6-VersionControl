#Michael Sanchez 
def encode(password):
    new_encode = list(str(password))
    new_encode = [int(i)+3 or int('0') == 3 for i in new_encode]         # compressed list incrementing each item. Added accountability for '0'
    new_encode = "".join(map(str, new_encode))         #revert each item in new_encode as str and join without comma
    return new_encode


def decode(password):
    decoded_password = ""
    for number in password:
        number = int(number) - 3
        if number < 0: number += 10
        decoded_password += str(number)
    return decoded_password

if __name__ == '__main__':
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    while True:
        option = int(input("\nPlease enter an option: "))

        if option == 1:
            password = int(input(f"Please enter your password to encode: "))
            new_encode = encode(password)
            print(f"Your encoded password is {new_encode}!")

        if option == 2:
            password = input(f"Please enter the password to decode: ")
            decoded_password = decode(password)
            print(f"The original password was {decoded_password}.")


        if option == 3:
            break
