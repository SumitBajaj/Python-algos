#Return the monthly payment for a loan amount amt, interest rate r, and loan duration in months n

#Loan_amount 
amt = 20000

#Loan_duration_in_months 
n = 60

#interest_rate 
r = .05

#calculate monthly payment
monthlyRepaymentCost = (r/12) * (1/(1-(1+r/12)**(-n)))*amt
print("Monthly payment is : ", monthlyRepaymentCost)