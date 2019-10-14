#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: October 2019
# This program outputs the month that corresponds to the integer inputted


def main():
    # This function outputs the month that corresponds to the integer inputted

    # input
    month_number = \
    int(input("Enter the number of a month (integer between 1-12): "))
    print("")

    # process
    if month_number == 1:
        print("The 1st month of the year is January.")
    elif month_number == 2:
        print("The 2nd month of the year is February.")
    elif month_number == 3:
        print("The 3rd month of the year is March.")
    elif month_number == 4:
        print("The 4th month of the year is April.")
    elif month_number == 5:
        print("The 5th month of the year is May.")
    elif month_number == 6:
        print("The 6th month of the year is June.")
    elif month_number == 7:
        print("The 7th month of the year is July.")
    elif month_number == 8:
        print("The 8th month of the year is August.")
    elif month_number == 9:
        print("The 9th month of the year is September.")
    elif month_number == 10:
        print("The 10th month of the year is October.")
    elif month_number == 11:
        print("The 11th month of the year is November.")
    elif month_number == 12:
        print("The 12th month of the year is December.")
    else:
        print("Invalid input!")


if __name__ == "__main__":
    main()
