#Return the total amount due for a loan after borrowing amount amt for n months with an interest rate of r%

def compound_interest(amt, r, n):

	# Calculates compound interest
	Total_Amount_Due = amt * (pow((1 + r/100),n/12))
	print("Total amount due for loan is ", Total_Amount_Due)

compound_interest(10000, 5, 36)
