# CHALLENGE NUMBER 16
# TOPIC: Conditional
# Shipping Accounts Program
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060798#overview


def validate_user(name):

    account_owners = ['Mike', 'Omar', 'Mau']
    if name in account_owners:
        return True
    else:
        return False


def ship_accounts(items_num):

    try:
        if 0 < items_num <= 100:
            price = 5.10
        elif 100 < items_num <= 500:
            price = 5
        elif 500 < items_num <= 1000:
            price = 4.95
        elif items_num > 1000:
            price = 4.80
    except:
        print("The items num added is not valid, please check!")
        return

    cost = items_num * price
    print("To ship " + str(int(items_num)) + " items it will cost you $" + str(round(cost, 2)) + " at $" + str(price) + " per item.")

    cust_dec = input("\nWould you like to place this order (y/n): ").lower().strip()
    if cust_dec == 'y':
        print("Okay. Shipping your " + str(int(items_num)) + " items.")
    elif cust_dec == 'n':
        print("Okay, no order is being placed at this time.")
    else:
        print("That option is not valid. Please check")

    return


if __name__ == '__main__':

    print("Welcome to the Shipping Accounts Program")
    name = input("\nHello, what is your username: ").title().strip()
    validation = validate_user(name)

    if validation:
        print("\nHello " + name + ". Welcome back to your account.")
        print("Current shipping prices are as follows: ")
        print("\nShipping orders 0 to 100:\t\t\t$5.10 each")
        print("Shipping orders 100 to 500:\t\t\t$5.00 each")
        print("Shipping orders 500 to 1000:\t\t$4.95 each")
        print("Shipping orders over 1000:\t\t\t$4.80 each")

        items_num = float(input("\nHow many items would you like to ship: "))
        ship_accounts(items_num)
    else:
        print("Sorry, you do not have an account with us. Goodbye")