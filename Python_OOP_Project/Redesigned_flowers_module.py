
from datetime import date
from datetime import datetime
import time

class Organization:
    """This class maintains a list of companies that are part of the organization and have the following methods:
    1. Create a New Company
    2. Modify Company Data
    3. Display Company Data in the Company_List"""

    def __init__(self,org_name = 'HQ'):
        self.org_name = org_name
        self._company_list= []

    def create_company(self):
        """This method is called by the Main Driver Program to create a new Company Instance.
        Error Checking is performed on user inputs for id and state. The method returns the Company
        Object to the calling program. The Company object is also appended to the self.company_list."""
        print("*******************************************************")
        print("*             Creating New Company                    *")
        print("*******************************************************")
        print("")
#Check to see if id is between 10000 and 99999
        while True:
            id=int(input("Enter Company ID (5 digit integer): "))
            if id >=10000 and id <=99999:
                break
            else:
                print("Invalid Entry")
        # print(id)
        name = input("Enter Company Name: ")
        # print(name)
        address = input("Enter Street Address: ")
        # print(address)
        city = input("Enter City: ")
#State cannot be more than 2 characters
        while True:
            state = input("Enter State (Eg: CA): ")
            if len(state) == 2:
                break
            else:
                print("Invalid Entry")
        print(id,name,address,city,state)
#create the Company instance
        comp = Company(id, name, address, city, state, 'USA')
#Append Company object to self.company_list
        self._company_list.append(comp)
        return comp

    def find_company_by_name(self,name):
        for c in self._company_list:
            if c._name == name:
                return c
        return None

    def modify_company_data(self):
        """This method iterates through self.company_list and allows a user
        to modify the data attributes."""
        count = 1
        for item in self._company_list:
            print("===== Company Data # {}=====".format(count))
            print("Company ID: ", item.id)
            print("Company Name: ", item.name)
            print("Address: ", item.address)
            print("City: ", item.city)
            print("State: ", item.state)
            print("Country: ", item.country)
            choice=input("Do you want to modify (Y/N): ")
            print("")
            if choice.lower() == 'y':
                item.name = input("Enter Company Name: ")
                item.address = input("Enter Street Address: ")
                item.city = input("Enter City: ")
                while True:
                    state = input("Enter State (Eg: CA): ")
                    if len(state) == 2:
                        item.state = state
                        break
                    else:
                        print("Invalid entry. Only 2 characters as in (Eg: CA)")
            count=count+1

    def display_company_data(self):
        """This method iterates through self.company_list and displays the company data."""
        count=1
        for item in self._company_list:
            print("===== Company Data # {}=====".format(count))
            print("Company ID: ", item.id)
            print("Company Name: ", item.name)
            print("Address: ", item.address)
            print("City: ", item.city)
            print("State: ", item.state)
            print("Country: ", item.country)
            count=count+1


class Company:
    """This class has all the attributes of a Company instance.
    Getters are Setters are implemented for the data attributes."""


    def __init__(self, comp_id=None, comp_name=None, comp_address=None, comp_city=None, comp_state=None, comp_country='USA'):
        self._comp_id = comp_id  #integer
        self._comp_name = comp_name  #string
        self._comp_address = comp_address  #string
        self._comp_city = comp_city  #string
        self._comp_state = comp_state  #2 character string
        self._comp_country = comp_country  #string. default = USA
        self._employee_list = []  #empty list to hold employee objects
        self._account_list = []  #empty list to hold account objects
        self._product_list = []  #empty list to hold product catalog

    @property
    def id(self):
        return self._comp_id

    @id.setter
    def id(self, new_id):
        if not isinstance(new_id, int):
            print("Please enter a valid company id")
        else:
            self._comp_id = new_id

    @property
    def name(self):
        return self._comp_name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            print("Please enter a valid company name")
        else:
            self._comp_name = new_name

    @property
    def address(self):
        return self._comp_address

    @address.setter
    def address(self, new_address):
        if not isinstance(new_address, str):
            print("Please enter a valid company name")
        else:
            self._comp_address = new_address

    @property
    def city(self):
        return self._comp_city

    @city.setter
    def city(self, new_city):
        if not isinstance(new_city, str):
            print("Please enter a valid company name")
        else:
            self._comp_city = new_city

    @property
    def state(self):
        return self._comp_state

    @state.setter
    def state(self, new_state):
        if not isinstance(new_state, str) and len(new_state) != 2:
            print("Please enter a valid state")
        else:
            self._comp_state = new_state

    @property
    def country(self):
        return self._comp_country

    @country.setter
    def country(self, new_country):
        if not isinstance(new_country, str):
            print("Please enter a valid country")
        else:
            self._comp_country = new_country

    def create_employees(self):
        """This method called by the driver program allows the user to create a new employee for a
        a Company. Error checking and validation is done and an Employee Instance is created."""

#Banner displays what company the employee is being created for
        print("*******************************************************")
        print("*       Creating Employees for company [{}]           *".format(self.name))
        print("*******************************************************")
        while True:
            id=int(input("Enter Employee ID (5 digit integer): "))
            if id >=10000 and id <=99999:
                break
            else:
                print("Invalid Entry")
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        title = input("Enter Job Title: ")
        address = input("Enter Street Address: ")
        while True:
            try:
                sal = float(input("Enter Monthly Salary (3500.00): "))
            except:
                print("Please try again. Enter a Valid Number")
            else:
                break
        while True:
            status = input("Enter Employee Status (Active or Inactive): ")
            if status.lower() =='active' or status.lower() == 'inactive':
                break
            else:
                print("Invalid Entry")
#Create a Employee Instance
        empl = Employees(id, lname, fname, title, sal, status)
        return empl

    def add_employee_to_company(self):
        """This method calls the create_employees method and appends the Employee Instance to
        self.employee_list."""
        x=self.create_employees()
        self._employee_list.append(x)
        self.display_employee_in_company()

    def display_employee_in_company(self):
        """This method iterates through self.employee_list and displays Employee data"""
        print("*********************************************************")
        print("Display Employee in Company [{}]                         ".format(self.name))
        print("*********************************************************")
        count=1
        for item in self._employee_list:
            print("\n===== Employee Data # {} =====".format(count))
            print("Employee ID: ", item._employee_id)
            print("First Name: ", item._employee_fname)
            print("Last Name: ", item._employee_lname)
            print("Job Title: ", item._employee_title)
            print("Monthly Salary: ", item._employee_mon_salary)
            print("Status: ", item._employee_status)
            count = count + 1

    def modify_employee_in_company(self):
        """This method allows a user to review all employee data for a company
        and change or modify data attributes."""

        print("********************************************************")
        print("Modify Employee in Company [{}]                         ".format(self.name))
        print("********************************************************")
        print("")
        print("============== Company Data ===================")
        print("***********************************************")
        print("Company ID:"+str(self.id)+" Company Name:"+str(self.name))
        print("Address:"+str(self.address))
        print("City:"+str(self.city)+" State:"+str(self.state)+" Country:"+self.country)
        print("***********************************************")
        print("")
        count = 1
        for index, item in enumerate(self._employee_list):
            print("\n===== Employee Data # {} =====".format(count))
            print("Employee ID: ", item._employee_id)
            print("First Name: ", item._employee_fname)
            print("Last Name: ", item._employee_lname)
            print("Job Title: ", item._employee_title)
            print("Monthly Salary: ", item._employee_mon_salary)
            print("Status: ", item._employee_status)
            while True:
                choice=input("Do you want to modify employees (Y/N): ")
                print("")
                if choice.lower() == 'y':
                    x = self.create_employees()
                    self._employee_list[index] = x
                    break
                else:
                    break
            count = count + 1

    def create_account(self):
        """This methods creates for each company the accounts to deposit, withdraw, transfer money
        and pay employees from."""

        print("*******************************************************")
        print("*       Creating Account for company [{}]             *".format(self.name))
        print("*******************************************************")
        print("")
        account_name = input("Enter Account Name (eg: Checking_Account_1): ")
        while True:
            bal=float(input("Enter starting balance amount: "))
            if bal > 0.0:
                break
            else:
                print("Invalid Entry")
        print(account_name,bal)
#Create a Account Instance
        accnt = Account(account_name, bal)
        print(accnt._name, accnt._balance)
        return accnt

    def add_account_to_company(self):
        """This method calls the create_account() and appends the Account Instance to
        self.account_list."""
        x = self.create_account()
        self._account_list.append(x)
        self.display_account_in_company()

    def display_account_in_company(self):
        """This method iterates through the self.account_list and displays the account data."""
        print("*********************************************************")
        print("Display Account in Company [{}]                         ".format(self.name))
        print("*********************************************************")
        print("")
        count=1
        for item in self._account_list:
            print("\n===== Account Data # {} =====".format(count))
            print("Account Name: ",item.account_name)
            print("Account Balance: ", item._balance)
            count = count + 1
        return self._account_list

    def get_date_time(self):
        """Returns a date and time stamp"""
        today=datetime.now()
        self.today_date=today.strftime("%m/%d/%Y")
        self.today_time=today.strftime("%H:%M:%S")
        return self.today_date,self.today_time

    def pay_employee_in_company(self,account):
        """Iterates through the employee_list and calls the account_withdraw() method.
        Note that a notes field is added to the withdrawl transaction to see who got paid."""
        for employee in self._employee_list:
            # print(employee.employee_id, employee.employee_mon_salary)
            notes = 'Payroll:' + str(employee._employee_id) + " " + str(employee._employee_fname) + " " + str(employee._employee_lname)
            # print(employee.employee_id, employee.employee_mon_salary, notes)
            account.account_withdraw(employee._employee_mon_salary, notes)

    def add_product_to_company(self):
        """This method adds a list of products to self.product_list."""
        prod_list = Product.set_up_product()
        self._product_list.append(prod_list)
        Product.browse_all_product(self)

#************************************************************

class Employees:
    """Employee class that has the data attributes for an Employees Instance."""

    def __init__(self, employee_id=None, employee_lname = None, employee_fname = None, employee_title = None, employee_mon_salary = None, employee_status = "Active"):
        self._employee_id = employee_id
        self._employee_lname = employee_lname
        self._employee_fname = employee_fname
        self._employee_title = employee_title
        self._employee_mon_salary = employee_mon_salary
        self._employee_status = employee_status

#************************************************

class Account:
    """This class has data attributes for Account Instance.
    Getters and Setters are implemented to manage the data attributes."""

    def __init__(self, name, balance):
        self._name=name  #name of account as string
        self._balance=balance  #balance as a float
        self._transaction=balance  #transaction amount
        self._transaction_type= 'First Deposit'  #transaction type field which can be "first deposit","deposit" or "withdrawl"
        today=datetime.now()
        self.today_date=today.strftime("%m/%d/%Y")  #date stamp
        self.today_time=today.strftime("%H:%M:%S")  #time stamp
        self._transaction_history=[]  #empty list to hold transaction history
        self._balance_history=[]  #empty list to hold balance history
        self._balance_history.append((self.today_date, self.today_time, self._balance))  #each time an account is created, update list
        self._transaction_history.append((self.today_date, self.today_time, self._transaction_type, self._transaction))  ##ach time an account is created, update list

    def get_date_time(self):
        """Get date and time stamp"""
        today=datetime.now()
        self.today_date=today.strftime("%m/%d/%Y")
        self.today_time=today.strftime("%H:%M:%S")
        return self.today_date,self.today_time

    @property
    def account_name(self):
        return self._name

    @account_name.setter
    def account_name(self, new_name):
        if not isinstance(new_name, str):
            print("Please enter a valid name")
        else:
            self._name = new_name

    @property
    def account_balance(self):
        return self._balance

    @account_balance.setter
    def account_balance(self, new_value):
        if not isinstance(new_name, float):
            print("Please enter a valid number")
        else:
            self._balance = new_value

    def account_deposit(self,amount):
        """This method when called updates account balance, updates transaction history,
        updates balance history and includes a date/time stamp."""
        self._transaction_type= "Deposit"
        self._balance= self._balance + amount
        self._transaction=amount
        self.show_transaction()
        self.show_balance()
        a,b=self.get_date_time()
        self._balance_history.append((a, b, self._balance))
        self._transaction_history.append((a, b, self._transaction_type, self._transaction))
        return

    def account_withdraw(self,amount, notes =""):
        """This method when called updates account balance, updates transaction history,
        updates balance history and includes a date/time stamp."""
#Notes field captures information on who got paid for salary when the account_withdraw method is called
        self._transaction_type= "Withdrawl" + " " + notes
        a,b=self.get_date_time()
#Error checking to prevent more than available balance being withdrawn
        if amount>self._balance:
            print("You cannot withdraw more than your available balance of {}".format(self._balance))
            self._transaction=0
        elif amount<0:
            print("You cannot withdraw negative amounts")
            self._transaction=0
        else:
            self._balance= self._balance - amount
            self._transaction=-amount
            self.notes = notes
            print("self.notes",self.notes)
            self.show_transaction()
            self.show_balance()
            self._balance_history.append((a, b, self._balance))
            self._transaction_history.append((a, b, self._transaction_type, self._transaction))
        return

    def money_transfer(self, to_whom, amount):
        """This method allows transfer of money from one account to another.
        After transfer is completed each account balance is updated,
        transaction history and balance history are also updated with a date and time stamp."""

        self._transaction_type= "Transfer"

        if amount <= self._balance:
            self._transaction=-amount
            self._balance= self._balance + self._transaction
            a,b=self.get_date_time()
            self._balance_history.append((a, b, self._balance))
            self._transaction_history.append((a, b, self._transaction_type, self._transaction))
            to_whom._balance= to_whom._balance - self._transaction
            to_whom._balance_history.append((a, b, to_whom._balance))
            to_whom._transaction_history.append((a, b, self._transaction_type, -self._transaction))
            print("Successfully transfered money from {} to {}".format(self._name, to_whom._name))
            print("Account Balance for {}:${} | Account Balance for {}:${}".format(self._name, self._balance, to_whom._name, to_whom._balance))
        else:
            print("Amount transferred cannot be more than {} available balance in {}".format(self._balance,self._name))
        return

    def show_transaction(self):
        print("********************************************************************")
        print("Account Name:{} | Transaction Type:{} | Amount:${}".format(self._name, self._transaction_type, self._transaction))

    def show_balance(self):
        print("Current Account Balance: ${}".format(self._balance))

    def show_balance_history(self):
        print("********************************************************************")
        print("Balance History for {}".format(self._name))
        print("********************************************************************")
        for dt,tm,amt in self._balance_history:
            print("Date:{} | Time:{} | Amount:${}".format(dt,tm,amt))

    def show_transaction_history(self):
        print("********************************************************************")
        print("Transaction History for {}".format(self._name))
        print("********************************************************************")
        for dt,tm,type,amt in self._transaction_history:
            print("Date:{} | Time:{} | Type:{} | Amount:${} |".format(dt,tm,type,amt))

#********************************************************************************************************

class Product:
    """This class contains data attributes for a product. For the purpose of demonstration, I have preset 5 products
    with part#, name, description, available qty and unit price.

    Use of Class Method is demonstrated here

    The methods in this class demonstrate simple searches commonly found in online sites such as:
    (1) Search by Name
    (2) Search by part#
    (3) Search by price range
    (4) See all product"""

    product_list = []

    @classmethod
    def set_up_product(cls):
        """Preset product data and append to the list"""
        product1 = Product('1001-P-148682','Fields of Europe','Our best-selling summer bouquet is gathered with fresh-picked blooms',15,69.99)
        product2 = Product('1001-P-176433','Vibrant Floral Medley','Our delightfully vibrant bouquet is filled with a medley of blooms',15,79.99)
        product3 = Product('1001-P-148793','Day Dream Bouquet','Our best-selling asian bouquet is gathered with fresh-picked blooms',15,59.99)
        product4 = Product('1001-P-176535','Budding Roses','Our delightfully vibrant bouquet is filled with a medley of rose blooms',15,99.99)
        product5 = Product('1001-P-158473','Classic All White','Pristine white roses, lilies and snapdragons are hand-gathered by our florists',15,89.99 )

        Product.product_list.append(product1)
        Product.product_list.append(product2)
        Product.product_list.append(product3)
        Product.product_list.append(product4)
        Product.product_list.append(product5)
        return Product.product_list

    @classmethod
    def browse_product_by_part(cls,company,filter_part):
        print("******************************************************************************************************************")
        print("Product Catalog for company {}".format(company.name))
        print("******************************************************************************************************************")
        print("")
        count=1
        flag = False
        for items in Product.product_list:
            if filter_part in items.product_numb:
                print('['+str(count)+']',"Product ID:",items.product_numb,"|","Product Name:", items.product_name,"|", "Available_Quantity:", items.product_inv,"|", "Price:$", items.product_price)
                print(items.product_desc)
                print("")
                count = count + 1
                flag = True
        if flag == False:
            print("Sorry no product exists. Please change selection criteria")

    @classmethod
    def browse_product_by_name(cls, company, filter_part):
        print("******************************************************************************************************************")
        print("Product Catalog for company {}".format(company.name))
        print("******************************************************************************************************************")
        print("")
        count=1
        flag = False
        for items in Product.product_list:
            if filter_part.lower() in items.product_name.lower():
                print('['+str(count)+']',"Product ID:",items.product_numb,"|","Product Name:", items.product_name,"|", "Available_Quantity:", items.product_inv,"|", "Price:$", items.product_price)
                print(items.product_desc)
                print("")
                count = count + 1
                flag = True
        if flag == False:
            print("Sorry no product exists. Please change selection criteria")


    @classmethod
    def browse_product_by_price_range(cls, price1, price2):
        print("******************************************************************************************************************")
        print("Product Catalog                                                                                                   ")
        print("******************************************************************************************************************")
        print("")
        count=1
        flag = False
        for items in Product.product_list:
            if items.product_price >= price1 and items.product_price <= price2:
                print('['+str(count)+']',"Product ID:",items.product_numb,"|","Product Name:", items.product_name,"|", "Available_Quantity:", items.product_inv,"|", "Price:$", items.product_price)
                print(items.product_desc)
                print("")
                count = count + 1
                flag = True
        if flag == False:
            print("Sorry no product exists. Please change selection criteria")

    @classmethod
    def browse_all_product(cls,self):
        print("******************************************************************************************************************")
        print("Product Catalog for [Company {}]".format(self.name))
        print("******************************************************************************************************************")
        print("")
        count=1
        for items in Product.product_list:
            print('['+str(count)+']',"Product ID:",items.product_numb,"|","Product Name:", items.product_name,"|", "Available_Quantity:", items.product_inv,"|", "Price:$", items.product_price)
            print(items.product_desc)
            print("")
            count = count + 1

#Note: Code below is not used but available for future enhancements where product data attributes can be modified and new product instances
#can be created.

    def __init__(self, product_numb, product_name, product_desc, product_inv, product_price):
        self.product_numb = product_numb
        self.product_name = product_name
        self.product_desc = product_desc
        self.product_price = product_price
        self.product_inv = product_inv
        # print(self.prod_list)

    def add_product_to_list(self):
        Product.product_list.append((self))

    @property
    def number(self):
        return self.product_numb

    @number.setter
    def number(self, new_number):
        if not isinstance(new_number, str):
            print("Please enter a valid product number")
        else:
            self.product_numb = new_number

    @property
    def price(self):
        return self.product_price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            print("Please enter a valid product price (eg- 49.55)")
        else:
            self.product_price = new_price

    @property
    def inventory(self):
        return self.product_inv

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            print("Please enter a valid product price (eg- 49.55)")
        else:
            self.product_price = new_price


































































































        # org = Organization('HQ')
# c1 = org.create_company()
# org.display_company_data()
#
# c2 = org.create_company()
# org.display_company_data()
#
#
# c1=org.find_company_by_name('abc')
# c1.add_employee_to_company()
# c1.display_employee_in_company()
#
# c1.modify_employee_in_company()
# c1.display_employee_in_company()
#
# c2=org.find_company_by_name('def')
# c2.add_employee_to_company()
# c2.display_employee_in_company()
#
# c2.modify_employee_in_company()
# c2.display_employee_in_company()
#
#
