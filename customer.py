class Customer:
    def __init__(self, customer_id, name, cnic, phone):
        self.customer_id = customer_id
        self.name = name
        self.cnic = cnic
        self.phone = phone
#df 
    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "cnic": self.cnic,
            "phone": self.phone
        }
