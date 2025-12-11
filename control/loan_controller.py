from services.database import Database
from models.loan import Loan
from utils.validator import Validator
from services.calculator import LoanCalculator

loan_db = Database("data/loans.json")

class LoanController:

    @staticmethod
    def add_loan():
        customer_id = input("Enter customer ID: ")
        amount = float(input("Enter loan amount: "))
        interest_rate = float(input("Enter interest rate (%): "))
        months = int(input("Enter months: "))

        loans = loan_db.read()
        loan_id = len(loans) + 1

        loan = Loan(loan_id, customer_id, amount, interest_rate, months)
        loans.append(loan.to_dict())
        loan_db.write(loans)

        installment = LoanCalculator.calculate_installment(amount, interest_rate, months)

        print(f"Loan added successfully. Monthly Installment = {installment} PKR")

    @staticmethod
    def list_loans():
        loans = loan_db.read()
        print("\n--- Loans List ---")
        for l in loans:
            print(l)
