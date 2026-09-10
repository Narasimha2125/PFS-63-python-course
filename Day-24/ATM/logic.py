data = {
    123456: {'pin': 1234, 'balance': 7000, 'history': []},
    234561: {'pin': 1234, 'balance': 5000, 'history': []},
    345612: {'pin': 1234, 'balance': 6000, 'history': []},
    456123: {'pin': 1234, 'balance': 9000, 'history': []}
}

def menu():
    print('[C]heck balance')
    print('[D]Deposit')
    print('[W]Withdraw')
    print('[V]View Transactions')
    print('[E]Exit')


def login():
    global acc_num
    acc_num = int(input("Enter the Account number: "))
    pin = int(input("Enter the Pin: "))

    if acc_num in data and data[acc_num]['pin'] == pin:
        print('Login Successful')
        return True
    else:
        print("Invalid login")
        return False

def checkbalance():
    print("Balance :", data[acc_num]['balance'])

def deposit():
    amount = int(input("Enter the Deposit Amount: "))
    data[acc_num]['balance'] += amount
    print(f'{amount} is successfully deposited.')
    data[acc_num]['history'].append(f'{amount} is deposited+++')


def withdraw():
    amount = int(input("Enter the withdraw Amount: "))
    if data[acc_num]['balance'] > amount: 
        data[acc_num]['balance'] -= amount
        print(f'{amount} is successfully Withdraw.')
        data[acc_num]['history'].append(f'{amount} is withdraw---')

    else:
            print("Insufficent Balance")


def viewtransactions():
    if data[acc_num]['history']:
        for i in data[acc_num]['history']:
            print(i)
    else:
        print("No Transaction History")



acc_num = 123456
print(data[acc_num]['pin'])
print(data[acc_num]['balance'])
print(data[acc_num]['history'])