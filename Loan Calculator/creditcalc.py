import math
import sys

# Calculate the number of months the user will repay
def num_monthly_payment(loan, monthly_payment, loan_interest):
    i = loan_interest / (12 * 100)
    num_months = math.log(monthly_payment / (monthly_payment - i * loan), 1 + i)
    n = math.ceil(num_months)
    years_months = divmod(n, 12)
    overpayment = int(monthly_payment * n - loan)
    if n < 12:
        print(f'It will take {int(n)} months to repay this loan')
    elif n % 12 == 0:
        print(f'It will take {int(n / 12)} years to repay this loan')
    else:
        print(f'It will take {int(years_months[0])} years and {int(years_months[1])} months to repay this loan!')

    print('Overpayment = ', overpayment)

# Calculate the amount user jas to pay monthly
def annuity(loan, num_periods, loan_interest):
    # loan = float(input('Enter the loan principal: '))
    # num_periods = float(input('Enter the number of periods: '))
    # loan_interest = float(input('Enter the loan interest: '))

    i = loan_interest / (12 * 100)

    a = math.ceil(loan * ((i * (1 + i)**num_periods) / ((1 + i)**num_periods-1)))
    overpayment = int((a * num_periods) - loan)

    print(f'Your monthly payment = {a}!')
    print('Overpayment = ', overpayment)

# Calculate the amount of users initially loan and overpay
def loan_principal(a, num_periods, loan_interest):

    i = loan_interest / (12 * 100)

    loan = int(a / ((i * (1 + i)**num_periods) / ((1 + i)**num_periods - 1)))
    overpayment = int(a * num_periods - loan)

    print(f'Your loan principal = {loan}!')
    print('Overpayment = ', overpayment)

# Calculate differentiated monthly payment
def differentiate(loan, num_periods, loan_interest):
    i = loan_interest / (12 * 100)
    overpayment = 0
    for j in range(1, num_periods + 1):
        diff_m = math.ceil((loan / num_periods) + i * (loan - ((loan * (j - 1)) / num_periods)))
        overpayment += diff_m
        print(f'Month {j}: payment is {(diff_m)}')
    print()
    print('Overpayment = ', int(overpayment - loan))

# Call other functions to do calculation
def calculate():
    
    args = sys.argv
    if len(args) != 5:
        print('Incorrect parameters')
    else:
        type = args[1].split('=')[1]
        principal = float(args[2].split('=')[1])
        periods = int(args[3].split('=')[1])
        payment = int(args[3].split('=')[1])
        interest = float(args[4].split('=')[1])
        payments = float(args[2].split('=')[1])

        l_args = []
        for i in args:
            l_args.append(i.split('=')[0][2:])
        l_args.pop(0)
        
        if 'interest' not in l_args:
            print('Incorrect parameters')
        elif periods <= 0 or interest <= 0:
            print('Incorrect parameters')
        else:
            
            if type == 'annuity':
                if 'periods' not in l_args:
                    num_monthly_payment(principal, payment, interest)
                elif 'payment' not in l_args:
                    annuity(principal, periods, interest)
                else:
                    loan_principal(payments, periods, interest)

            elif type == 'diff':
                if 'payment' in l_args:
                    print('Incorrect parameters')
                else:
                    differentiate(principal, periods, interest)


calculate()