principal_amount=float(input('enter the car principal value')) #50000
rate_of_interest = float(input('enter the rate of interest per year')) #3 %
total_months = int(input("number of months to repay the loan")) #24
montly_emi = int(input("monthly emi paid")) #1000

loan_rate=rate_of_interest/100/12
for i in range(100):
    interest_value = principal_amount * loan_rate
    total_amount_owned = principal_amount+interest_value
    if(total_amount_owned-montly_emi < 0):
        print('amount after the last payment is '+str(total_amount_owned) )
        print('you paid of the load in ', i+1, "months")
        break
    principal_amount = total_amount_owned - montly_emi

    print("montly emi paid, "+ str(montly_emi) + " of which, interest paid "+str(interest_value), end= '')
    print(" principal remaining "+ str(total_amount_owned))