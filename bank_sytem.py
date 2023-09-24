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
        new_account = f'1111-{random.randint(1,10000000 ):010}'
        account_numbers.add(new_account)
    return list(account_numbers)  # to convert to list


def get_account_by_number(customer_list , account_number_to_find):

    for customer in customer_list:
        if customer.account_number == account_number_to_find:
            print(f'Account {account_number_to_find} found.')
            break
        elif customer.account_number > account_number_to_find:
            print(f'Account {account_number_to_find} not found.')
            break
    
    else:
        print(f'Account {account_number_to_find} not found.')

          
if __name__ == "__main__":
    customer_list = []
    num_customers = 10**7
    start = time.time()
    for i in range(1,num_customers+1):
        customer = Customer(name=f"Customer{i}",
                            account_number = generate_account_numbers(i)[0],
                            balance=random.randint(1,10000),
                            created=datetime.now(),
                            last_updated=datetime.now())
        customer_list.append(customer)
    end = time.time()
    
    print(*customer_list, sep = "\n")
    print(f'Time taken to create {num_customers} customers: {(end - start) * 1000} ms')

    start = time.time()
    customer_list.sort(key=lambda customer: customer.account_number,reverse = True)
    end = time.time()
    
    for n in customer_list:
        print(n.account_number) #print account numbers after sortering
    print (f"Time taken to sort {num_customers} customers is:{(end-start)*1000} ms")
   
    
