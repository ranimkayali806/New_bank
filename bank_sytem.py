import time
from datetime import datetime
import random
from time import sleep



class Customer:
    def __init__(self, name,created,last_updated, account_number, balance,birthday=None):
        self.name = name
        self.created = created
        self.last_updated = last_updated
        
        self.account_number = account_number
        self.balance = balance

        if birthday is None:
            self.assign_random_birthday()
        else:
            self.birthday = birthday

    
   
    def __repr__(self):
        return f"Customer(name: {self.name}, account_number:{self.account_number},balance:{self.balance},birthday:{self.birthday})"
        
    def account_created(self):
        created = datetime.now()
        return created
    
    def account_last_updated(self):
        last_updated = datetime.now()
        return last_updated
    
   
    def customer_balance(self,balance):
        self.balance= []
        balance = f"{random.randint(1,10000)}"
        return balance

    def assign_random_birthday(self):
      
        year = random.randint(1992,2000)
        month = random.randint(1,12)
        day = random.randint(1,31)
  
        if month == 4 or month == 6 or month == 9 or month == 11:
            day = random.randint(1,30)
        elif month == 2:
            day = random.randint(1,28)
        else:
            day = random.randint(1,31)
        

        if month >= 10:
            month = month
        else:
            month = f"0{month}"

        if day >= 10:
            day = day
        else:
            day = f"0{day}"
        date_str= f"{year}-{month}-{day}"
        self.birthday= datetime.strptime(date_str,"%Y-%m-%d")
        

def generate_account_numbers(num_accounts):    #randomly
    account_numbers = set()      # för att vi vill inte duppletter använder set()
    while len(account_numbers) < num_accounts:
        account_number = f'1111-{random.randint(1,10000000 ):010}'
        account_numbers.add(account_number)
    return list(account_numbers)

def bubble_sort(account_numbers):
    n = len(account_numbers)
    for i in range(n):
        swapp = False
        for j in range(0, n-i-1):
            if  account_numbers [j] >  account_numbers [j+1]:
                account_numbers [j],  account_numbers [j+1] =  account_numbers [j+1],  account_numbers [j]
                swapp = True
        if not swapp:
            break
    

if __name__ == "__main__":
    customer_list = []
    num_customers = 10**7
    start = time.time()
    for i in range(1,num_customers+1):
 
        account_number = generate_account_numbers(num_accounts=i)
        customer = Customer(name=f"Customer{i}",
                            account_number = account_number,
                            balance=random.randint(1,10000),
                            created=datetime.now(),
                            last_updated=datetime.now())
        customer_list.append(customer)
    end = time.time()
    for i in customer_list:
        print(i)
       
    print(f'Time taken to create { num_customers} customers: {(end - start) * 1000} ms')
