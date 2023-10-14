import datetime

class Bank:
    def __init__(self):
        self.users = []
        self.admins = []  
        self.bank_balance = 0
        self.total_loan=0
        self.loan_feature = True


class User:
    account_number=101
    def __init__(self, name, email,address, account_type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.account_number = User.account_number
        User.account_number += 1
        self.balance = 0
        self.transaction_history = []
        self.loan_count =0


    def deposit(self, amount):
        if amount>0:
            self.balance +=amount
            islamic_balnk.bank_balance +=amount
            timestamp = datetime.datetime.now()
            self.transaction_history.append(f'Deposit amount {amount} time {timestamp}')
        print(f"successfully deposit {amount}")
    
    def withdraw(self, w_amount):
        if w_amount>self.balance:
            print(f"Withdrawal amount exceeded")
        else:
            self.balance -=w_amount
            islamic_balnk.bank_balance -=w_amount
            timestamp = datetime.datetime.now()
            self.transaction_history.append(f'withdraw amount {w_amount} time {timestamp}')
            print(f'withdraw successful {w_amount}')
    
    def available_balance(self):
        print(f'total_balance is {self.balance}')
    
    def loan_from_the_bank(self, l_amount):
        if islamic_balnk.loan_feature:
            if self.loan_count<2:
                if l_amount>0:
                    self.balance +=l_amount
                    islamic_balnk.total_loan+=l_amount
                    self.loan_count +=1
                    timestamp = datetime.datetime.now()
                    self.transaction_history.append(f'you take loan from bank . loan amount is {l_amount}, time {timestamp}')
                    print(f"Loan of ${l_amount} taken successfully")
            else:
                print(f"you get loan maximum two time you cross this limit")
    
    def transfer_amount(self, amount, recive_account):
        print(recive_account.balance, amount, self.balance, recive_account.account_number)
        
        if amount<self.balance:
            for user in  islamic_balnk.users:
                if recive_account.account_number == user.account_number:
                    self.balance -=amount
                    recive_account.balance +=amount
                    self.transaction_history.append(f"Transferred ${amount} to account {recive_account.account_number}")
                    print(f"Transferred ${amount} to account {recive_account.account_number}")
                    return
            else:
                print(f'Account does not exist')
        else:
            print(f'"Insufficient amount {amount}"')




islamic_balnk=Bank()

class Admin:
    def __init__(self, name, password) -> None:
        self.name=name
        self.password=password
        islamic_balnk.admins.append((name, password))
    def create_user_account(self, name, email, address, account_type):
        if account_type=='saving':
            account = User(name, email, address, account_type)
            islamic_balnk.users.append(account)
            print(f'user account create successfully done {name}')
            return account
        elif account_type =='current':
            account = User(name, email, address, account_type)
            islamic_balnk.users.append(account)
            print(f'user account create successfully done {name}')
            return account
        else:
            print(f'Invalid account Type {account_type} please enter saving or current type')

    def delete_user_account(self, account_number):
        for user in islamic_balnk.users:
            if user.account_number == account_number:
                islamic_balnk.users.remove(user)
                return
           
        print("User account not found")

    
    def see_all_user_account_list(self):
        for user in islamic_balnk.users:
            print(f'user accountNumber: {user.account_number} userName: {user.name}')
    
    def total_bank_balance(self):
        print(f'bank_balance: {islamic_balnk.bank_balance}')
    
    def total_loan_amount(self):
        print(f'Total loan amount {islamic_balnk.total_loan}')

    def loan_feature_on_off(self):
        islamic_balnk.loan_feature = not islamic_balnk.loan_feature

    




print('-------------General output ---------')

admin1=Admin('rana', 1234)

user1=admin1.create_user_account('tanjid', 'tanjid@gmail.com', 'kushtia', 'saving')
user2=admin1.create_user_account('tan', 'tan@gmail.com', 'kushtia_dhaka', 'current')
user3=admin1.create_user_account('tamana', 'tan@gmail.com', 'dhaka', 'current')

user1.deposit(234234)
user1.withdraw(453)
user1.available_balance()
user1.loan_from_the_bank(23)
user1.transfer_amount(500,user2)
print(user1.balance)
print(user2.balance)
for i in range(len(user1.transaction_history)):
    print(user1.transaction_history[i])

admin1.see_all_user_account_list()
admin1.total_bank_balance()
for user in islamic_balnk.users:
    print(user.account_number)

admin1.delete_user_account(103)



print('-------------Loop output  ---------')


currentUser=None

while True:
    if currentUser==None:
        print('Welcome to our Islamic bank:')
        print('Are you Admin/User:')
        ch=input('type admin/user:')
        if(ch=="admin"):
            print("For test purpose admin password is : 1234")
            password=int(input('Please Enter Your password:'))
            print(password, islamic_balnk.admins[0][1])
            if(islamic_balnk.admins[0][1]==password):
                currentUser=ch

            else:
                print('please provide valid password')
        elif ch=='user':
            acc_no=int(input('Enter your account Number: '))
            for user in islamic_balnk.users:
                if acc_no==user.account_number:
                    currentUser=user
                    print(f'welcome {user.name}')
        else:
            print("Enter admin or user ")
    else:
        print(f'Welcome {currentUser}')
        if currentUser=='admin':
                print('1.Create user Account')
                print('2.See all user Account list')
                print('3.Delete any user Account')
                print('4.Check total bank balance')
                print('5.Check total loan amount')
                print('6.ON or Off loan feature')
                print('7.Again start')
                print('8.Exit')

                ch=int(input('Enter serial number:'))
                if ch==1:
                   no= int(input('how many account you create: '))
                   for i in range(no):
                        name=input('enter user name:')
                        email=input('enter user email:')
                        address=input('enter user address:')
                        type=input('enter user account type (saving/current):')
                        admin1.create_user_account(name, email, address, type)
                elif ch==2: 
                    admin1.see_all_user_account_list()
                elif ch==3:
                    acc_no=int(input('please Enter user account Number:'))
                    admin1.delete_user_account(acc_no)
                elif ch==4:
                    admin1.total_bank_balance()
                elif ch==5:
                    admin1.total_loan_amount()
                elif ch==6:
                    admin1.loan_feature_on_off()
                elif ch==7:
                    currentUser=None
                elif ch==8:
                    break
        else:
            print(f'Welcome {currentUser.name}')

            print("1. Deposit money your account")
            print("2. Withdraw money from your account")
            print("3. Your Available balance")
            print("4. loan_from_the_bank")
            print("5. Transfer money one account to another account")
            print("6. transition_history")
            print("7. Exit")

            ch=int((input('Enter serial No: ')))
            if ch==1:
                amount=int(input('Enter your Amount'))

                currentUser.deposit(amount)
            elif ch==2:
                amount=int(input('Enter your Amount'))

                currentUser.withdraw(amount)
            elif ch==3:
                currentUser.available_balance()
            elif ch==4:
                amount=int(input('Enter your Amount'))
                currentUser.loan_from_the_bank(amount)
            elif ch==4:
                amount=int(input('Enter your Amount'))
                currentUser.loan_from_the_bank(amount)
            elif ch==5:
                acc_no=int(input('Enter receiver account Number: '))
                amount=int(input('Enter your Amount'))
                receiver=None
                for user in islamic_balnk.users:
                    if acc_no==user.account_number:
                        receiver=user
                currentUser.transfer_amount(amount,receiver)
            elif ch==6:
                for i in range(len(currentUser.transaction_history)):
                    print(currentUser.transaction_history[i])
            elif ch==7:
                break



















    

