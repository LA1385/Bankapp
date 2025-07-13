#creating an ATM machine prototype with python
print('Please Insert your card properly')
input('press enter to proceed if done.')
from ass import deposit,withdrawal,checkbalance
def ATM(operation=deposit,choice='continue'):
   print('Welcome back Ahmad,We are ready for your service today\n' \
   'Your current balance is $3000')
   while True:
      operation=int(input('1. Deposit:\n'
      '2. Withdraw\n'
      '3. Checkbalance\n'
      'Enter your operation:'))
      if operation==1:
         tempamount=int(input('enter your amount:'))
         pin=int(input('enter your PIN:'))
         if pin==1385:
            deposit(tempamount)
            print('your action is successful')
         else:
            print('PIN is incorrect,please try again')

      elif operation==2:
         wamount=int(input('enter your amount:'))
         pin=int(input('enter your PIN:'))
         if pin==1385:
            withdrawal(wamount)
         else:
            print('PIN is incorrect,please try again')
      elif operation==3:
         checkbalance()
      else:
         print("we don't offer such service,Thank you. ")

      choice=str(input('Do you want to continue Y/N:'))
      if choice=='y':
         continue
      else:
         break
         
    
ATM(operation='deposit')
print('Thank you for the service.')