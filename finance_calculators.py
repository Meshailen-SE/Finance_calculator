#Task 12
#Compulsory Task 1
#12/02/2020
#Meshailen Chetty

#imported math
import math

#created an opening statement and asked the user to choose and option of (investment or bond)
#displayed the input on seperate line with a new tab (\t) and a new line with (\n) 
calculation_type = input("Choose either \'Investment\' or \'bond\' from the menu below proceed:\n"" \n investment \t - to calculate the amount of interest you'll earn on interest.\n bond \t         - to calculate the amount you'll have to pay on a home loan.\n")

#created an if statement for 'investment' and inside the if statement i asked the user to input certain inputs 
#and created variables that added the users inputs or divided or multiplied
#casted a string to a float
#created two options if the user chose investment, which are simple or compound interest
if calculation_type.lower() == "investment":
    amount_invest = float(input("What is the total amount that you are depositing?\n"))
    interest_invest = (input("What is the interest rate as a percentage(%)?(enter the number only)\n"))
    interest_percentage = float(interest_invest) / 100
    years_invest = float(input("How many years do you plan to invest for?\n"))
    interest = input("What type of interest plan would you like? (simple or compound)\n")
    if interest.lower() == "simple":
        simple_formula = float(amount_invest * (1 + interest_percentage * years_invest))
        print(f"Your simple interest works out to be R{simple_formula:.2f}")

    if interest.lower() == "compound":
            compound_formula = float(amount_invest * math.pow(( 1 + interest_percentage), years_invest))
            print(f"Your compound interest works out to be R{compound_formula:.2f}")

#created elif statement if the user chose the bond option
# asked the user a series of inputs like years , amount and percentage
# used the bond repayment formula and added all the variables in the formula to calc the amount
# and printed the final amount 

elif calculation_type.lower() == "bond":
    property_value = float(input("What is present value of your house?\n "))
    interest_bond = float(input("What is the interest rate as a percentage(%)?(enter the number only)\n"))
    interest_bond_percentage = interest_bond / 100
    months_bond = float(input("How many months do you plan on repaying the bond? "))
    repayment = ((property_value * math.pow((interest_bond/12)+1,months_bond))*(interest_bond/12)) / ((math.pow(interest_bond/12 +1, months_bond)-1))
    final_repay = repayment/12
    print(f"Your monthly installments work out to R{final_repay:.2f}")