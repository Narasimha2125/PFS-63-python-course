import logic as lg

if lg.login():
    print("Welcome to the ATM")
    while True:
        lg.menu()
        ch = input("Enter the Choice: ").upper()
        if ch == "C":
            lg.checkbalance()
        elif ch == 'D':
            lg.deposit()
        elif ch == "W":
            lg.withdraw()
        elif ch == 'V':
            lg.viewtransactions()
        elif ch == 'E':
            print("Thank you & Visit again!")
            break
        else:
            print("Enter Valid Choice")