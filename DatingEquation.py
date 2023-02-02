#The Dating Equation
# "Never date anyone youger than half your age plus seven"

#Input variables
yourAge = int(input("How old are you? "))
crushesAge = int(input("How old is the person you have a crush on: "))

#Implementation of our algorithm
minimumAgeAllowed = (yourAge/2) + 7

#Do the thing
if yourAge >= 18 and crushesAge >= 18:
    if crushesAge < minimumAgeAllowed:
        print("You shouldn't be dating. You are super creepy!")
    elif crushesAge > minimumAgeAllowed:
        print("That is socially acceptable.")
    elif crushesAge == yourAge:
        print("You can date. That is socially acceptable.")
    else:
        print("EDGECASE!")
else:
    print("THIS IS NOT OKAY!")
