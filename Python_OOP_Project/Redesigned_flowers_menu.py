
#This is the driver program that provides a UI for BizOPPs Application.
#The Menu guides the user through selections and provides error checking where
#appropriate.
#The Menu design is a combination of a flat menu structure and a nested menu structure
#to demonstrate seamless program flow between modules.
#Key features of BizOPPs are:
#1. Ability to create, modify and view companies inside an Organization
#2. Ability to create, modify and view for each of the companies
#2. Ability to create, modify and view accounts for each of the companies
#4. Ability to pay employees
#5. Ability to view and search product catalog


import time
from Redesigned_flowers_module import Organization
from Redesigned_flowers_module import Company
from Redesigned_flowers_module import Employees
from Redesigned_flowers_module import Account
from Redesigned_flowers_module import Product


def admin_menu():
    """This is the driver function or the main function that navigates the user through
    the selections. Error checking is provided where appropriate."""

    display_menu()  # display_menu function displays the menu choices for the user

    org = Organization()  # initialize the Class Organization

    while True:
        try:
            selection=int(input("Enter main menu choice: "))
#Option 1 is creating a new company
            if selection == 1:
                c1 = org.create_company()  #call the class method create_company()
                print("")
                print("Successfully created company")
                org.display_company_data()
                time.sleep(1)
                print("")
                display_menu()
#Option 2 is modifying a company
            elif selection == 2:
                time.sleep(1)
#Logic to ensure that a company exists before modification
                if len(org._company_list)>0:
                    org.modify_company_data()
                    print("Successfully modifed company")
                    org.display_company_data()
                else:
                    print("Invalid selection. You must first create a company to modify")
                display_menu()
#Option 3 is viewing a company
            elif selection == 3:
                time.sleep(1)
#Logic to ensure that a company exists before viewing
                if len(org._company_list)>0:
                    org.display_company_data()
                else:
                    print("Invalid selection. You must first create a company to view")
                time.sleep(1)
                display_menu()
#Option 4 is creating a employee
            elif selection == 4:
                time.sleep(1)
                if len(org._company_list)<1:
                    print("Invalid selection. You must first create a company to create employees")
                    admin_menu()
#Display choices of company to create employees
                org.display_company_data()
#Error checking on user inputs
                while True:
                    try:
                        choice = int(input("Enter # of Company: "))
                        if choice <= 0 or choice > len(org._company_list):
                            raise Exception
                    except Exception as e:
                        print("Please try again. Choice cannot be less than zero and more than number of companies")
                    except:
                        print("Please try again. Enter a valid number")
                    else:
                        break
#Get the company object from the company_list
                x=org._company_list[choice - 1]
#Call the add_employee_to_company method to create employees in the company selected
                x.add_employee_to_company()
                time.sleep(1)
                display_menu()
#Option 5 is modify employee data
            elif selection == 5:
                time.sleep(1)
                if len(org._company_list)<1:
                    print("Invalid selection. You must first create a company to modify employees")
                    admin_menu()
#Display choices of company to create employees
                org.display_company_data()
#Error checking on user inputs
                while True:
                    try:
                        choice = int(input("Enter # of Company: "))
                        if choice <= 0 or choice > len(org._company_list):
                            raise Exception
                    except Exception as e:
                        print("Please try again. Choice cannot be less than zero and more than number of companies")
                    except:
                        print("Please try again. Enter a valid number")
                    else:
                        break
                x=org._company_list[choice - 1]
#Error checking to ensure an employee exists first
                if len(x._employee_list)<1:
                    print("You must create employees before paying salary.")
                    x.add_employee_to_company()
#Call the modify_employee_in_company method to modify employees in the company selected
                x.modify_employee_in_company()
                time.sleep(1)
                display_menu()
#Option 6 is view employee data
            elif selection == 6:
                time.sleep(1)
                if len(org._company_list)<1:
                    print("Invalid selection. You must first create a company to create employees")
                    admin_menu()
                org.display_company_data()
                while True:
                    try:
                        choice = int(input("Enter # of Company: "))
                        if choice <= 0 or choice > len(org._company_list):
                            raise Exception
                    except Exception as e:
                        print("Please try again. Choice cannot be less than zero and more than number of companies")
                    except:
                        print("Please try again. Enter a valid number")
                    else:
                        break
                x=org._company_list[choice - 1]
                x.display_employee_in_company()
                time.sleep(1)
                display_menu()
#Option 7 is pay employee option
            elif selection == 7:
                time.sleep(1)
#Error chceking to ensure a company exists first
                if len(org._company_list)<1:
                    print("Invalid selection. You must first create a company to create employees")
                    admin_menu()
                org.display_company_data()
                while True:
                    try:
                        choice = int(input("Enter # of Company: "))
                        if choice <= 0 or choice > len(org._company_list):
                            raise Exception
                    except Exception as e:
                        print("Please try again. Choice cannot be less than zero or more than number of companies")
                    except:
                        print("Please try again. Enter a valid number")
                    else:
                        break
                x = org._company_list[choice - 1]
#Error checking to ensure an employee exists first
                if len(x._employee_list)<1:
                    print("You must create employees before paying salary.")
                    x.add_employee_to_company()
#Error checking to ensure an account exists first
                if len(x._account_list) < 1:
                    print("you must create an account before paying salary.")
                    account_menu(x)
                num = x.display_account_in_company()
                while True:
                    try:
                        choice = int(input("Enter choice of account to pay employee: "))
                        if choice <= 0 or choice > len(num):
                            raise Exception
                    except Exception as e:
                        print("Please try again. Choice cannot be less than zero or more than number of accounts")
                    except:
                        print("Please try again. Enter a valid number")
                    else:
                        break
                y = x._account_list[choice - 1]
                x.pay_employee_in_company(y)
                display_menu()
#Option 8 is a nested account menu selection
            elif selection == 8:
                time.sleep(1)
#Error chceking to ensure a company exists first
                if len(org._company_list)<1:
                    print("Invalid selection. You must first create a company to create accounts")
                    admin_menu()
#Select the company to add, modify and view accounts
                org.display_company_data()
                print("")
                while True:
                    try:
                        choice = int(input("Enter # of Company: "))
                        if choice <= 0 or choice > len(org._company_list):
                            raise Exception
                    except Exception as e:
                        print("Please try again. Choice cannot be less than zero and more than number of companies")
                    except:
                        print("Please try again. Enter a valid number")
                    else:
                        break
                x = org._company_list[choice - 1]
#Call account_menu function to display the account_menu choices
                account_menu(x)
                time.sleep(1)
                display_menu()
#Option 9 is a nested product catalog menu selection
            elif selection == 9:
                time.sleep(1)
#Error chceking to ensure a company exists first
                if len(org._company_list)<1:
                    print("Invalid selection. You must first create a company to add and manage products")
                    admin_menu()
#Select the company to add and view product catalog
                org.display_company_data()
                while True:
                    try:
                        choice = int(input("Enter # of Company: "))
                        if choice <= 0 or choice > len(org._company_list):
                            raise Exception
                    except Exception as e:
                        print("Please try again. Choice cannot be less than zero and more than number of companies")
                    except:
                        print("Please try again. Enter a valid number")
                    else:
                        break
                x = org._company_list[choice - 1]
#Call product_menu function to display the product_menu choices
                product_menu(x)
                display_menu()
#Quit the application
            elif selection == 0:
                print("Have a good day")
                break
            else:
                print("Invalid choice. Please try again.")
                display_menu()
        except ValueError:
            print("Invalid choice. Please try again.")
            display_menu()
    exit()

def display_menu():
    """Display menu displays an elegant UI for the user choices and is called by the main driver function."""
    print("|********************************************************|")
    print("|          W e l c o m e   T o    B i z O O P            |")
    print("|          World's # 1 Enterprise Application            |")
    print("|  Powered by Python and Built on Object Oriented Design |")
    print("|********************************************************|")

    time.sleep(1)

    print("")
    print("|==================Company Module========================|")
    print("| [1] Set new company:                                   |")
    print("| [2] Modify company:                                    |")
    print("| [3] View company:                                      |")
    print("|==================Employee Module=======================|")
    print("| [4] Create employee                                    |")
    print("| [5] Modify employee                                    |")
    print("| [6] View employee                                      |")
    print("| [7] Pay Employee                                       |")
    print("|==================Account Module========================|")
    print("| [8] Account Menu                                       |")
    print("|==================Product Module========================|")
    print("| [9] Product Menu                                       |")
    print("|========================================================|")
    print("| [0] Quit Program                                       |")
    print("|========================================================|")
    print("")

def product_menu(company):
    """product_menu is called by main driver program and offers choices for the user
    to add products to the company, view products, view product by name,
    view product by price range, view product by product number."""

    print("|********************************************************|")
    print("|                 Product Menu Options                   |")
    print("|********************************************************|")
    print("| [1] Add Products to Company                            |")
    print("| [2] View All Products                                  |")
    print("| [3] View Product by Name                               |")
    print("| [4] View Product by Price Range                        |")
    print("| [5] View Product by Product Number                     |")
    print("| [0] Return to Main Menu                                |")
    print("|********************************************************|")
    print("")

    selection=int(input("Enter choice: "))

#Option 1 adds product to a company by calling the method
    if selection == 1:
        company.add_product_to_company()
        product_menu(company)
#Option 2 is browse all products
    elif selection == 2:
        Product.browse_all_product(company)
        product_menu(company)
#Option 3 is search products by name
    elif selection == 3:
        name = input("Enter product name for search (eg: rose): ")
        Product.browse_product_by_name(company,name)
        product_menu(company)
#Option 4 is search products by price range
    elif selection == 4:
        start_price = int(input("Enter starting price (eg: 59.99):"))
        end_price = int(input("Enter starting price (eg: 99.99):"))
        Product.browse_product_by_price_range(start_price,end_price)
        product_menu(company)
#Option 5 is search product by part number
    elif selection == 5:
        part_number = input("Enter product number for search (eg: 148682): ")
        Product.browse_product_by_part(company, part_number)
        product_menu(company)
    elif selection == 0:
        return
    else:
        print("Invalid choice. Please try again")

def account_menu(company):
    """This function allows a user to create an account, make deposit, make withdrawl,
    transfer money between accounts and show account history."""

    print("|********************************************************|")
    print("|                 Account Menu Options                   |")
    print("|********************************************************|")
    print("| [1] Create Account                                     |")
    print("| [2] Make Deposit                                       |")
    print("| [3] Make withdrawl                                     |")
    print("| [4] Make money transfer                                |")
    print("| [5] Show history                                       |")
    print("| [0] Return to Main Menu                                |")
    print("|********************************************************|")
    print("")

    selection=int(input("Enter account menu choice: "))

#Option 1 is create account
    if selection == 1:
        company.add_account_to_company()  # call method to create company
        print("Successfully created account")
        account_menu(company)
#Option 2 is deposit to account
    elif selection == 2:
        num = company.display_account_in_company()
#Error checking to ensure an account exists before deposit
        if len(num) == 0:
            print("You must create an account before deposit")
            print("")
            account_menu(company)
#Error checking for account selection and deposit amount
        while True:
            try:
                print("")
                choice = int(input("Enter choice of account to deposit: "))
                if choice <= 0 or choice > len(num):
                    raise Exception
            except Exception as e:
                print("Please try again. Choice cannot be less than zero or more than number of accounts")
            except:
                print("Please try again. Enter a valid number")
            else:
                break
        y = company._account_list[choice - 1]
        while True:
            try:
                amt = float(input("Enter deposit amount (eg: 4500.00): "))
            except:
                print("Please try again. Enter a valid number")
            else:
                while amt <= 0:
                    amt = float(input("Enter a valid deposit amount (must be greater than 0): "))
                break
        y.account_deposit(amt)
        account_menu(company)
#Option 3 is make withdrawl
    elif selection == 3:
        num = company.display_account_in_company()
#Error checking to ensure an account exists before withdrawl
        if len(num) == 0:
            print("You must create an account before withdrawl")
            print("")
            account_menu(company)
        print("")
#Error checking for account selection and withdrawl amount
        while True:
            try:
                choice = int(input("Enter choice of account to withdraw: "))
                if choice <= 0 or choice > len(num):
                    raise Exception
            except Exception as e:
                print("Please try again. Choice cannot be less than zero or more than number of accounts")
            except:
                print("Please try again. Enter a valid number")
            else:
                break
        y = company._account_list[choice - 1]
        while True:
            try:
                amt = float(input("Enter withdrawl amount (eg: 4500.00): "))
                while amt > y._balance:
                    amt = float(input("Cannot withdraw more than available balance of {}. Please reenter a valid amount: ".format(y._balance)))
            except:
                print("Please try again. Enter a valid number")
            else:
                break
        y.account_withdraw(amt)
        account_menu(company)
#Option 4 is money transfer
    elif selection == 4:
        account_list = company.display_account_in_company()
#Error checking to ensure atleast 2 accounts exist for transfer
        if len(account_list) < 2:
            print("You must have atleast 2 accounts for money transfer")
            print("")
            account_menu(company)
        print("")
#Error checking for account selection and transfer amount
        while True:
            try:
                choice1=int(input("Press Choice for From Account:"))
                choice2=int(input("Press Choice for To Account:"))
                if (choice1 <= 0 or choice1 >len(account_list) or choice2 <= 0 or choice2 > len(account_list) or choice1 == choice2):
                    raise Exception
            except Exception as e:
                print("Please try again. Choice cannot be less than zero, more than number of companies or equal")
            except:
                print("Please try again. Enter a valid value")
            else:
                break
        while True:
            try:
                amt=float(input("Enter transfer amount (Eg: 1000.00): "))
            except:
                print("Please try again. Enter a valid value")
            else:
                break
        first = account_list[choice1-1]
        second = account_list[choice2-1]
        first.money_transfer(second,amt)
        account_menu(company)
#Option 5 show history
    elif selection == 5:
        for x in company._account_list:
            x.show_transaction_history()
            x.show_balance_history()
        account_menu(company)
#Option 0 return control to main menu
    elif selection == 0:
        return
    else:
        print("Invalid choice. Please try again")
        account_menu(company)
























admin_menu()