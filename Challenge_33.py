# CHALLENGE NUMBER 33
# TOPIC: Funct
# Bank Program
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060888#overview


def bank_deposit(user_name, user_info_dict, access_account, money_amount):
    user_info_dict[access_account] += money_amount
    print("\nDeposited ${} into {}'s {} account.".format(money_amount, user_name, access_account))
    return


def bank_withdrawal(user_name, user_info_dict, access_account, money_amount):
    if money_amount <= user_info_dict[access_account]:
        user_info_dict[access_account] -= money_amount
        print("\nWithdrawed ${} from {}'s {} account.".format(money_amount, user_name, access_account))
    else:
        print("\nYou do not have that amount available.")
    return


def print_account_info(user_info_dict):

    print("\nCurrent Account Information")
    for key, value in user_info_dict.items():
        if key == 'Name':
            print("{}: {}".format(key, value))
        else:
            print("{}: ${}".format(key, value))

    return


def main():
    print("Welcome to the Python First National Bank.")
    name = input("\nHello, what is your name: ").strip().title()
    savings = float(input("How much money would you like to set up your savings account with: ").strip())
    checking = float(input("How much money would you like to set up your checking account with: ").strip())
    user_info = {'Name': name, 'Savings': savings, 'Checking': checking}

    flag_program = True
    while flag_program:
        print_account_info(user_info)
        access_account = input("\nWhat account would you like to access (Savings or Checking): ").strip().title()
        if access_account == 'Savings' or access_account == 'Checking':
            transaction_type = input("What type of transaction would you like to make (Deposit or Withdrawal): ").strip().title()
            money = float(input("How much money: ").strip())
            if transaction_type == 'Deposit':
                bank_deposit(name, user_info, access_account, money)
            elif transaction_type == 'Withdrawal':
                bank_withdrawal(name, user_info, access_account, money)
            else:
                print("Invalid option. Try again")
            run_again = input("Would you like to make another transaction (y/n): ").strip().lower()
            if run_again == 'n':
                flag_program = False
                print("Thank you. Have a great day!")
            elif run_again != 'y':
                print("Invalid option. Try again!")
        else:
            print("Invalid option. Try again!")
            run_again = input("Would you like to make another transaction (y/n): ").strip().lower()
            if run_again == 'n':
                flag_program = False
                print("Thank you. Have a great day!")
            elif run_again != 'y':
                print("Invalid option. Try again!")

    return


if __name__ == '__main__':
    main()