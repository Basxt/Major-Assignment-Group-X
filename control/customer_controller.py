from services.database import Database
from models.customer import Customer
from utils.validator import Validator

db = Database("data/customers.json")

class CustomerController:

    @staticmethod
    def add_customer():
        name = input("Enter customer name: ")
        cnic = input("Enter CNIC: ")
        phone = input("Enter phone: ")

        if not Validator.check_empty(name):
            print("Invalid name!")
            return

        customers = db.read()
        customer_id = len(customers) + 1

        cust = Customer(customer_id, name, cnic, phone)
        customers.append(cust.to_dict())
        db.write(customers)
        print("Customer added successfully.")

    @staticmethod
    def list_customers():
        customers = db.read()
        print("\n--- Customer List ---")
        for c in customers:
            print(c)
