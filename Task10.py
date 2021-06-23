print("**********Task 10**********\n")
class Bank:
      def __init__(self,n,m,balance=0.0) :
             self.acno=n
             self.name=m
             self.balance =balance
      def deposit(self,amt):
            self.balance+=amt
            return self.balance
      def withdraw(self,amt) :
            if amt>self.balance :
                print('\nBalance amt is less,so cannot withdraw')
            else :
                self.balance-=amt
            return self.balance


accno=input('Enter  Acct no.:   ')
name=input('Enter name  :   ')
#bal=float(input('Enter balance :   '))
b=Bank(accno,name)
flag = 'yes'
while flag=='yes':
  print('d - deposit,  w- withdrawl ' )
  ch = input('Enter choice  :  ')
  if ch == 'd':
       amt = float(input('Enter amount to be deposited  :   ') )
       print('Balance amount  :  ',b.deposit(amt))
  else :
       amt = float(input('Enter amount to be withdrawn  :  '))
       print('Balance amount  :  ',b.withdraw(amt)  )
  flag= input('\nDo you  want to continue yes/no   :  ')
print("\n------------Task 10 Completed Succesfully-----------")