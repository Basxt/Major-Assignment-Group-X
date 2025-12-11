class Loan:
    def __init__(self, loan_id, customer_id, amount, interest, months, status="approved"):
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.amount = amount
        self.interest = interest
        self.months = months
        self.status = status
#sd
    def to_dict(self):
        return {
            "loan_id": self.loan_id,
            "customer_id": self.customer_id,
            "amount": self.amount,
            "interest": self.interest,
            "months": self.months,
            "status": self.status
        }
