#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
#print()

# get input from the user
print()
miles_driven = float(input("Enter miles driven:         "))
gallons_used = float(input("Enter gallons of gas used:  "))
cost_gallon = float(input("Enter cost per gallonn:     "))
print()

if miles_driven <= 0:
    print("Miles driven must be greater than zero. Please try again.")
elif gallons_used <= 0:
    print("Gallons used must be greater than zero. Please try again.")
elif cost_gallon <= 0:
    print("Cost per gallon must be greater than zero. Please try again.")
else:
    # calculate and display miles per gallon
    mpg = round((miles_driven / gallons_used), 2)
    print("Miles Per Gallon:          ", mpg)
    tgc = round((gallons_used * cost_gallon), 2)
    print("Total Gas Cost:            ", tgc)
    cpm = round((cost_gallon * gallons_used / miles_driven), 1)
    print("Cost Per Mile:             ", cpm)
    print()

#loop    
yn = (input("Get entries for another trip (y/n)?"))
while yn == 'y':
    # get input from the user
    print()
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_gallon = float(input("Enter cost per gallonn:     "))
    print()
    
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:          ", mpg)
        tgc = round((gallons_used * cost_gallon), 2)
        print("Total Gas Cost:            ", tgc)
        cpm = round((cost_gallon * gallons_used / miles_driven), 1)
        print("Cost Per Mile:             ", cpm)
        print()
        yn = (input("Get entries for another trip (y/n)?"))

print()
print("Bye")



