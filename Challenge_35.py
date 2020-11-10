# CHALLENGE NUMBER 35
# TOPIC: Funct
# Loan Calculator
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060904#overview
import matplotlib.pyplot as plt


def approve_loan(loan_amount, interest, monthly_payment):

    min_monthly_amount = loan_amount * (interest / 100)
    if monthly_payment <= min_monthly_amount:
        print("\nYou will NEVER pay off your loan!!!\nYou cannot get ahead of the interest! :-(")
        return False
    return True


def display_info(loan_amount, interest, monthly_payment, months_paid=0, money_paid=0):
    print("\n----Loan information after {} months----".format(months_paid))
    print("Principal: {}\nRate: {}\nMonthly Payment: {}\nMoney Paid: {}".format(loan_amount, interest, monthly_payment, money_paid))
    return


def payment_simulator(loan_amount, interest, monthly_payment):

    total_debt_history = []
    months_debt_history = []
    money_paid = 0
    months_paid = 0
    total_amount = (loan_amount * (interest / 100)) + loan_amount

    active_loan = True
    total_debt_history.append(total_amount)
    months_debt_history.append(months_paid)
    while active_loan:
        months_paid += 1
        months_debt_history.append(months_paid)
        money_paid += monthly_payment
        total_amount -= monthly_payment
        total_debt_history.append(total_amount)
        display_info(total_amount, interest, monthly_payment, months_paid, money_paid)
        if total_amount <= 0:
            active_loan = False
            print("\nCongratulations, you have paid the loan!")
            print("You have a positive amount of ${}".format(abs(total_amount)))

    return months_debt_history, total_debt_history


def main():
    print("Welcome to the Loan Calculator App")
    loan_amount = float(input("\nEnter the loan amount: ").strip())
    interest_rate = float(input("Enter the interest rate: ").strip())
    monthly_payment = int(input("Enter the desired monthly payment amount: ").strip())
    display_info(loan_amount, interest_rate, monthly_payment)
    if approve_loan(loan_amount, interest_rate, monthly_payment):
        input("Press 'Enter' to begin paying off your loan.")
        months_record, payments_records = payment_simulator(loan_amount, interest_rate, monthly_payment)
        plt.plot(months_record, payments_records)
        plt.show()

    return


if __name__ == '__main__':
    main()