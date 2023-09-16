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




def generate_account_number(index):
    return f"1111-{index:010}"
start_index = 1
end_index = 10000000


def get_account_by_number(customer_dict , account_number_to_find):
      customer = customer_dict.get(account_number_to_find, None)
      if customer:
           return customer
      else:
          return None
     

   

if __name__ == "__main__":
    #customer_list = []
    num_customers = 10**7
    start = time.perf_counter()
    customers_dict = {f"1111-{i:010}": Customer(name=f"Customer{i}", 
                                                          account_number=f"1111-{i:010}",
                                                          balance=random.randint(1,10000),
                                                          created=datetime.now(),
                                                          last_updated=datetime.now()) for i in range(1, num_customers+1)}
    
  
    end = time.perf_counter()
   
    for key, value in customers_dict.items():
        print(f"{key}: {value}")
    print(f'Time taken to create { num_customers} customers: {(end - start) * 1000} ms')




    start = time.perf_counter()
    account_to_find1 = '1111-0000001000'
    get_account_by_number(customers_dict, account_to_find1)
    end = time.perf_counter()
    print(f'Time taken to find account {account_to_find1}: {(end - start) * 1000} ms')



    start = time.perf_counter()
    account_to_find2 = '1111-0009999999'
    get_account_by_number(customers_dict, account_to_find2)
    end =time.perf_counter()
    print(f'Time taken to find account {account_to_find2}: {(end - start) * 1000} ms')

