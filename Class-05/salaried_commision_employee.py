from commision_employee import CommisionEmployee

class SalariedCommisionEmployee(CommisionEmployee):
    def __init__(self, f_name, l_name, social_security, gross_sales, commision_rate, base_salary):
        super().__init__(f_name, l_name, social_security, gross_sales, commision_rate)
        self.base_salary = base_salary

    def earning(self):
        return super().earning() + self.base_salary
    
    def __str__(self):
        return f"Salaried {super().__str__()}\n"
    
    
# sce1 = SalariedCommisionEmployee("Sai Lochan", "Dash", 4177, 120000, 0.05, 10000)
# print(sce1)