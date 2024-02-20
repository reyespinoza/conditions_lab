#creating a lump sum loan payment calculator

def nl():
    print("\n")


print("Welcome to the Lump Sum Loan Payment Calculator")

nl()

FirstName = input("What is your first name? ")  #User is to input first name
LoanAmount = int(input("What is your loan amount? "))  #user is to input whatever loan amount
IntRate = float(input("What is your interest rate (in decimal form - 15% = .15): "))  #user is to input whatever interest rate they want, but in decimal format
LumpSum = int(LoanAmount * 1 * IntRate + LoanAmount) #formula to calculate total sum of loan after interest

nl()

if IntRate <= .10:
    print("That\'s a great interest rate!")
elif .10 < IntRate <= .20:
    print("That interest rate is getting a little high!")
elif .20 < IntRate <= .25:
    print("That interest rate is really not that good!")
elif IntRate > .25:
    print("That interest rate - you are REALLY getting ripped off!")

nl()

if LumpSum >= 100000:
    print("That\'s a lot of money - you will need a payment plan...")

nl()