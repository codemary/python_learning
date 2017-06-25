"""This program is used to create and manage a bank account"""
import random
import sys


def get_name():
    """get valid name"""
    name = input("Enter Name:")
    if name == "":
        print("Invalid name! Please enter a valid name")
        return get_name()
    else:
        return name


def get_address():
    """get valid address"""
    address = input("Enter Address:")
    if address == "":
        print("Invalid address! Please enter a valid address")
        return get_address()
    else:
        return address


def get_account_num(digits):
    """generating random account"""
    lower = 10**(digits - 1)
    upper = 10**digits - 1
    return random.randint(lower, upper)


def get_phone_num():
    """get valid phone number"""
    phone_num = input("Enter Phone Number:")
    if len(phone_num) != 10:
        print("Invalid Number! Please enter a valid phone number:")
        return get_phone_num()
    else:
        return phone_num


def get_age():
    """get valid phone number using recursive function"""
    age = input("Enter Age:")
    if age == "":
        print("Invalid Age! Please enter a non-empty age!")
        return get_age()

    if not age.isdigit():
        print("Invalid Age! Please enter an integer age!")
        return get_age()

    # convert string to integer
    age_int = int(age)

    if age_int >= 18 and age_int <= 125:
        return age_int
    else:
        print("Invalid Age! Please enter age between 18-125!")
        return get_age()


def get_gender():
    """get valid gender"""
    gender = input("Enter Gender(M/F):")
    if gender == "M" or gender == "m" or gender == "F" or gender == "f":
        return gender
    print("Invalid Gender! Please enter valid gender(M/F or m/f):")
    return get_gender()


def print_account_details(account):
    """to print account details"""
    print("\n")
    print("Account Details==>>>>>\n")
    print("Name:%s" % account['name'])
    print("Age:%s" % account['age'])
    print("Gender:%s" % account['gender'])
    print("Address:%s" % account['address'])
    print("Phone:%s" % account['phone_num'])
    print("Account No:%s" % account['accountNum'])
    print("Balance:%s" % account['balance'])


def new_account():
    """details to be filled if new account is made"""
    print("=============")
    print("Enter your details as follows")

    account = {
        'name': get_name(), 'age': get_age(), 'gender': get_gender(),
        'address': get_address(), 'phone_num': get_phone_num(),
        'accountNum': get_account_num(7), 'balance': 0
    }

    print_account_details(account)
    return account


def existing_account(account):
    """managing the account if the account already exists"""
    print_account_details(account)
    manage_account(account)


def withdrawal(account):
    """calculating withdrawal amount"""
    print("=============")
    withdrawal_amount = int(input("Enter amount to be withdrawn:"))
    if withdrawal_amount > account['balance']:
        print("You have insufficient amount in your account! Enter valid amount. 0 to go back.")
        return withdrawal(account)
    else:
        account['balance'] -= withdrawal_amount
        print("Amount withdrawn: The current balance for account %s(%d) is %d Rs." %
              (account["name"], account["accountNum"], account["balance"]))


def balance_enq(account):
    """calculating account balance"""
    print("=============")
    print("\n")
    print("The current balance for account %s(%d) is %d Rs." %
          (account["name"], account["accountNum"], account["balance"]))


def deposit(account):
    """calculating deposited amount"""
    print("=============")
    deposit_amount = int(input("Enter amount to be deposited:"))
    account['balance'] += deposit_amount
    print("Amount deposited: The current balance for account %s(%d)is %d Rs." %
          (account["name"], account["accountNum"], account["balance"]))


def manage_account(account):
    """to manage account"""
    print("\n")
    print("**Account Menu")
    print("=============")
    print("1.Balance Enquiry\n2.Withdrawal\n3.Deposit\n4.Back")

    choice = input("Enter Choice:")
    if choice == "1":
        balance_enq(account)
    elif choice == "2":
        withdrawal(account)
    elif choice == "3":
        deposit(account)
    elif choice == "4":
        # go back to the main menu
        return
    else:
        print("Invalid Choice! Please select again!")
        return manage_account(account)

    print("Thank You!")
    # stay at the account menu
    return manage_account(account)


def main(account=None):
    """main function with a default argument"""
    print("\n")
    print("*Main Menu")
    print("=============")
    print("1.New Account\n2.Existing Account\n3.Exit")

    choice = input("Enter Choice:")
    if choice == "1":
        account = new_account()
    elif choice == "2":
        if not account:
            account = {'name': "noname", 'age': 0, 'gender': "",
                       'address': "", 'phone_num': "", 'accountNum': 0, 'balance': 0}

        existing_account(account)
    elif choice == "3":
        # exit successfully
        sys.exit(0)
    else:
        print("Invalid Choice! Please select again!")
        return main(account)

    return main(account)


if __name__ == "__main__":
    main()
