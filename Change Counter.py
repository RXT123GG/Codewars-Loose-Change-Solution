#Codewars "Loose Change!" solution.
# Defines a function that takes a string of change-inputs, seperates them into a list, sorts them by type and adds to a counter
# then returns a formatted output in $0.00 format as a string
# https://www.codewars.com/kata/57e1857d333d8e0f76002169/solutions/python 


def change_count(change):
    changeList = change.split()
    moneyCounter = 0.00
    for change in changeList:
        if change == "penny":
            moneyCounter += 0.01
        elif change == "nickel":
            moneyCounter += 0.05
        elif change == "dime":
            moneyCounter += 0.10
        elif change == "quarter":
            moneyCounter += 0.25
        elif change == "dollar":
            moneyCounter += 1.00
        else:
            print(str(change))
                     
    return(f"${moneyCounter:.2f}")