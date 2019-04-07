P=input("Enter the amount of principal originally deposited into the account: ")
r=input("Enter the annual interest rate paid by the account:")
n=input("Enter the number of times per year that the interest is compound:")
t=input("Enter the number of years the account will be left to earn interest:")
def calculateCompoundInterest(P,r,n,t):
    A=P*(1+r*n)*n*t
    print("The amount of money that will be in the account after ", int(t)," years: ",A)
calculateCompoundInterest(float(P),float(r),float(n),float(t))