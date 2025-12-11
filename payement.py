class Payment:
    def __init__(self, payment_id, loan_id, amount):
        self.payment_id = payment_id
        self.loan_id = loan_id
        self.amount = amount
#sd
    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "loan_id": self.loan_id,
            "amount": self.amount
        }
