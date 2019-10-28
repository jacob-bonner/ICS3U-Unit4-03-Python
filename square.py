#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: October 2019
# This program finds squares up to the specified number


def main():
    # This function finds squares up to the specified number

    # Input
    positive_integer = int(input("Enter a number here (positive integer): "))

    # Process
    for counter in range(positive_integer + 1):
        square = counter**2
        print("{0}² = {1}".format(counter, square))


if __name__ == "__main__":
    main()
