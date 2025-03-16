class CommisionEmployee(object):
    def __init__(self, f_name, l_name, social_security, gross_sales, commision_rate):
        self.f_name = f_name
        self.l_name = l_name
        self.social_security = social_security
        self.gross_sales = gross_sales
        self.commision_rate = commision_rate

    @property
    def gross_sales(self):
        return self._gross_sales
    @gross_sales.setter
    def gross_sales(self, value):
        if value < 0:
            raise ValueError("Gross Sales cannot be negative.")
        self._gross_sales = value

    @property
    def commision_rate(self):
        return self._commision_rate
    @commision_rate.setter
    def commision_rate(self, value):
        if not (0 <= value <= 1):
            raise ValueError("Commission rate must be between 0 and 1.")
        self._commision_rate = value

    def earning(self):
        return self.commision_rate * self.gross_sales
    
    def __str__(self):
        return f"Commissioned Employee:\nName: {self.f_name} {self.l_name}\nEarnings: {self.earning()}\n"

# ce1 = CommisionEmployee("Sai Lochan", "Dash", 4177, 120000, 0.05)
# print(ce1)

