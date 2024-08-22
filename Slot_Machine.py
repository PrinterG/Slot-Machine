MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

def deposit():
    while True:
        amount = input("How much you wanna deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("deposit should be more than $0")
        else:
            print("please enter a valid deposit")
            
    return amount

def get_number_of_lines():
    while True:
        number = input("How many lines? ")
        if number.isdigit():
            number = int(number)
            if 0 < number <= MAX_LINES:
                break
            else:
                print(f"there are only {MAX_LINES} lines")
        else:
            print("please enter a valid number of lines")
            
    return number

def get_bet():
    while True:
        amount = input("How much you wanna bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"bet should be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a valid bet")
            
    return amount

def main():
    balance = deposit()
    bet = get_bet()
    lines = get_number_of_lines()
    
main()