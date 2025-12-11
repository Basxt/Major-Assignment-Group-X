from services.database import Database
from models.payment import Payment

payment_db = Database("data/payments.json")

class PaymentController:

    @staticmethod
    def add_payment():
        loan_id = input("Enter loan ID: ")
        amount = float(input("Enter paid amount: "))

        payments = payment_db.read()
        payment_id = len(payments) + 1

        pay = Payment(payment_id, loan_id, amount)
        payments.append(pay.to_dict())
        payment_db.write(payments)

        print("Payment added.")

    @staticmethod
    def list_payments():
        payments = payment_db.read()
        print("\n--- Payment List ---")
        for p in payments:
            print(p)
