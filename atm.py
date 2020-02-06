savings = 0
funds = 0
current = 12000.00
command=''
while command != "quit":
    command= input('[UBA BANK SECURE SERVER]:')
    break


def deposit(funds):
    deposit_process= funds + savings
    return deposit_process
    return(f"Hello your account has been credited with {deposit_process} succesfully")


def withdraw(funds):
    return("[UBA BANK SECURE SERVER]:Please take your cash")

def check_balance():
    return (f"[UBA BANK SECURE SERVER]:you have{savings}in your account")

if command == "deposit":
    load = input("[UBA BANK SECURE SERVER]:How much do you want to deposit?:")
    print (deposit(load))
elif command == "withdraw":
    load = input("[UBA BANK SECURE SERVER]:How much do you want to withdraw?:")
    print (withdraw(load))
if command == "check balance":
    print (check_balance())


