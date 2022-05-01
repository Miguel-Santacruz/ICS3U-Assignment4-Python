#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Apr 2022
# This program checks for discount


def main():
    # This function calculates discount

    # input
    string = input("Amount of units: ")

    # process & output
    print("")
    try:
        number = int(string)
        if number < 0:
            print("invalid amount of units.")
        elif number > 1000:
            subtotal = number * 100
            discount = subtotal * 0.1
            HST = (subtotal - discount) * 0.13
            total = subtotal - discount + HST
            print("Your total is ${}".format(total))
        else:
            subtotal = number * 100
            HST = subtotal * 0.13
            total = subtotal + HST
            print("Your total is ${}".format(total))
    except Exception:
        print("{} is not a valid number of units.".format(string))

    print("\nDone.")


if __name__ == "__main__":
    main()
