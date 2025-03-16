from salaried_commision_employee import SalariedCommisionEmployee
from commision_employee import CommisionEmployee

class Duck:
    def __init__(self):
        pass
    
    def earning(self):
        return f"Earning is 100000.\n"
    
    def __str__(self):
        return f"I am a well paid Duck.\n"
    
d = Duck()
ce1 = CommisionEmployee("Sai Lochan", "Dash", 4177, 120000, 0.05)
sce1 = SalariedCommisionEmployee("Sai Lochan", "Dash", 4177, 120000, 0.05, 10000)


L = [ce1, sce1, d]
for employee in L:
    e = employee.earning()
    print(e)
    print(employee)

# In Python, if something looks like a duck and talks like a duck, IT IS A DUCK.