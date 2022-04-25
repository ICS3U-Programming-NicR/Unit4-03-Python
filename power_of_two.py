#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: April 24 2022
# Find the power of numbers


def main():
    # Get inputs
    user_num_str = input("What range of numbers do you want to find the power of: ")
    # try catch
    try:
        user_num = int(user_num_str)
    except:
        print("You have to input integers greater that 0")
        main()
    for counter in range(user_num + 1):
        print("{}^2 = {}".format(counter, counter**2))


if __name__ == "__main__":
    main()
