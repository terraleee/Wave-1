toonie = 200
loonie = 100
quarter = 25
dime = 10
nickel = 5
penny = 1

cents = int(input("Enter the number of cents: "))

print("Your change consists of:")

print(" ", cents // toonie, "toonie(s).")
cents = cents % toonie

print(" ", cents // loonie, "loonie(s).")
cents = cents % loonie

print(" ", cents // quarter, "quarter(s).")
cents = cents % quarter

print(" ", cents // dime, "dime(s).")
cents = cents % dime

print(" ", cents // nickel, "nickel(s).")
cents = cents % nickel

print(" ", cents // penny, "pennie(s).")
