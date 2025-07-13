num = 3000
#created a function for Depositing money
def deposit(amount):
    global num
    num += amount

#created a function for withdrawal
def withdrawal(amount):
    global num
    if num>=amount:
        num-=amount
        print('transaction successful')
    else:
        print('insufficient balance')

#creating a function for checking account balance
def checkbalance():
    pin=int(input('Enter your pin:'))
    if pin==1385:
        print(f"current balance:${num}")
    else:
        print('incorrect pin,please try again')






        
