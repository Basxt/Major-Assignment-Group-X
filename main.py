from utils.menu import Menu
from controllers.customer_controller import CustomerController
from controllers.loan_controller import LoanController
from controllers.payment_controller import PaymentController
from controllers.report_controller import ReportController

while True:
    choice = Menu.main_menu()

    if choice == "1":
        CustomerController.add_customer()
        CustomerController.list_customers()

    elif choice == "2":
        LoanController.add_loan()
        LoanController.list_loans()

    elif choice == "3":
        PaymentController.add_payment()
        PaymentController.list_payments()

    elif choice == "4":
        ReportController.full_report()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
        #