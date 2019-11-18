#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    monthly_investment = float(input("Enter monthly investment:\t"))
    while monthly_investment <= 0:
        print("Entry must be greater then 0. Please try again.")
        monthly_investment = float(input("Enter monthly investment:\t"))
        continue
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    while yearly_interest_rate <= 0 or yearly_interest_rate >= 15:
        print("Entry must be greater then 0 and less than or equal to 15.")
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        continue
    years = int(input("Enter number of years:\t\t"))
    while years <= 0 or years >= 50:
        print("Entry must be greater then 0 and less than or equal to 50.")
        years = int(input("Enter number of years:\t"))
        continue

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(1, months + 1):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        if i % 12 == 0:
            print("Year = " + str(i // 12) + "\tFuture value = \t" + str(round(future_value, 2)))
    print()


    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
