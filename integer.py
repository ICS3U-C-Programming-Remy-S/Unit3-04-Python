#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct 19, 2023
# This program will ask the user
# for a number and will tell them
# if it is positive, negative or 0


def main():
    # Get the user guess and display message
    print("This program will ask the user for a integer")
    print("then it will display if it is positive, negative or 0.")
    user_int = int(input("Please enter a integer: "))

    # Check if the user integer is positive, negative or 0
    if user_int > 0:
        # Display if the user integer is positive
        print("\n{} is positive".format(user_int))

    elif user_int < 0:
        # Display if the user integer is negative
        print("\n{} is negative".format(user_int))

    else:
        # Display if the user is wrong
        print("\nYour integer is 0")


if __name__ == "__main__":
    main()
