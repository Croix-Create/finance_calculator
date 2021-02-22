import math

print("Choose either 'investment' or 'bond' to procede: \n"
    "investment - to calculate the amount of money you'll earn on an integer\n"
    "bond       - to caclculate the amount of money you'll pay on a home loan")

option = input().lower()

    # Defining functions investsimple with parameters amount, inter_invest and no years 
def investsimple(amount, inter_invest, no_years):
    # A = P*(1+r*t) - simple interest calculation
    inter_simp = float(amount)*(1 + float(inter_invest) / 100 * float(no_years))
    print(str(round(inter_simp, 2)) + '\n')
    
    # Defining investcompound with parameters in order to call the function(s) later on
def investcompound(amounts, inter_invest, no_years):
    # A = P* math.pow((1+r),t) - compound interest calculation
    inter_comp = (amounts) * math.pow(float(1) + inter_invest / 100, no_years)
    print(str(round(inter_comp, 2)) + '\n')
   
    # If user chooses investment they will be given the option to calculate either simple or compound interest
if (option == "investment"): 
    amount = float(input("What is the investment amount?\n"))
    inter_invest = float(input("What is the interest rate?\n"))
    no_years = float(input("Please enter the number of years you want to invest for.\n"))
    interest = input("Would you like 'simple' or 'compound'?\n").lower()
    #here we  call the functions investsimple & investcompound to refer back to the scope in the upper code block to calculate
    if (interest == "simple"):
        investsimple(amount, inter_invest, no_years)
    elif (interest == "compound"):
        investcompound(amount, inter_invest, no_years)
    # If the option is equal to bond we will request new inputs in order to run the bond calculation, rounded to the last two digits

elif (option == "bond"):
    value = float(input("What is the present value of the house?\n"))
    bond_interest = float(input("What is the interest? E.g 7\n"))
    repay_bond = float(input("In how many months will you repay?\n"))
    #bond calculation
    repay_per_month = (bond_interest/100 * value)/(1 - (1+bond_interest/100)**(-repay_bond))
    print(str(round(repay_per_month, 2)))
