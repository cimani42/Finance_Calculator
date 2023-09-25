import math

simple_compound_interest_url = ("https://www.investopedia.com/articles/investing/020614/learn-simple-and-compound-inter"
                                "est.asp")
simple_compound_interest_link = "Click here for the simple and compound interest explanation."
simple_compound_explained = f"{simple_compound_interest_link}:{simple_compound_interest_url}"

# r is the interest rate above divided by 100, giving a percentage.
# P is the amount that the user deposits
# t is the number of years that the money is being invested.
# A is the total amount once the interest has been applied

# simple interest formula... A = P(1 + r * t)
# compound interest formula... A = P(1 + r) ^ t or P * math.pow((1+r),t)

# Pv is the present value of the house
# i is the monthly interest rate, found by dividing annual interest by 12.
# n is the number of months the bond will be repaid.

print("Choose either 'investment' or 'bond' from the below to proceed.\n")
prompt = input("investment - to calculate the amount of interest you'll earn on your investment\n"
               "bond - to calculate the amount you'll have to ay on a home loan. \n")

answer = prompt.lower()

if answer == "investment":
    prompt2 = input("Do you want to calculate 'simple interest' or 'compound interest'?\n ")
    answer2 = prompt2.lower()

    # hyperlinks to help describe the difference between simple and compound interest.
    print("Want to know more about the difference between simple and compound interest?\n"
          f"{simple_compound_explained}. \n")

    interest = int(input("Enter the annual interest rate. \n"))
    deposit = (input("Enter the amount of the investment. \n"))
    years = input("Enter the number of years you want to invest for. \n")

    r = interest / 100
    P = float(deposit)
    t = int(years)

    if answer2 == "simple interest" or "simple":
        simple_interest = P*(1 + r * t)
        A = round(simple_interest, 2)
        difference = round((A - P), 2)
        print(f"You have a total £ {A:,} from the investment. ")
        print(f"You have made a a profit of £{difference:,}")
    elif answer2 == "compound interest" or "compound":
        compound_interest = P * math.pow((1 + r), t)
        A = round(compound_interest, 2)
        difference2 = round((A - P), 2)
        print(f"You have a total £ {A:,} from the investment. ")
        print(f"You have made a a profit of £{difference2:,}")
    else:
        print("Invalid Response. Please try again responding either 'compound interest' or 'simple interest'"
              "to continue.\n")

elif answer == "bond":
    present_value = float(input("Enter the present value of the house. \n"))
    repayment = float(input("Enter the number of months the repayment will be made. \n"))
    interest2 = int(input("Enter the annual interest rate. \n"))/100

    Pv = present_value
    i = (interest2 / 12)
    n = repayment

    bond_repayment = (i*Pv)/(1 - math.pow((1+i), (-n)))
    x = round(bond_repayment, 2)
    print(f"You will have to repay £ {x:,} each month.")
else:
    print("Invalid response. Please try again responding either 'investment' or 'bond' to continue. ")
