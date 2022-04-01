#Task2


account_balance = 100
#user_pin = 3322



def withdraw_cash():
    withdrawal_amount = int(input("Please tell us how much money you would like to withdraw:"))
    end_balance = account_balance - withdrawal_amount
    try:
        if withdrawal_amount > account_balance:
            raise Exception

    except:
        print('You do not have so much money!Try again')
        withdraw_cash()

    else:
        print('Withdrawal accepted. You have {} £ left.'.format(end_balance))
        quit()


def enter_pin():
    pin_attempts = 0
    for number in range(0, 3):
        user_pin = int(input('Welcome to CFG Bank! Please enter your 4-digit pin:'))
        try:
            if user_pin != 3322:
                return 'Please try again'

                raise Exception

        except:

            def incorrect_pin():
                try:
                    if pin_attempts >= 3:
                        raise Exception
                except:
                    print("You entered the wrong pin 3 times. You cannot proceed further. Please contact your bank")
                    quit()

            incorrect_pin()

        else:
            print("Correct pin.")
            withdraw_cash()


enter_pin()
