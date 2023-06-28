# This is to convert from kilometers to miles

def convertToKilo(kilometers):
    miles = kilometers * 0.624
    return miles

yourKilometer = float(input("Enter a kilometer you want to convert: "))
print("It is", round(convertToKilo(yourKilometer),2), "miles.")
