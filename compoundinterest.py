interest = 0.04
balance = float(input("Enter the amount of money deposited: ")) 
interestearned = interest * balance

year1 = interestearned + balance
year2 = year1 * interest + year1
year3 = year2 * interest +year2

print("The amount in the savings account after one year is", round(year1, 2), "dollars.")
print("The amount in the savings account after two years is",round(year2, 2), "dollars.")
print("The amount in the savings account after three years is",round(year3, 2), "dollars.")