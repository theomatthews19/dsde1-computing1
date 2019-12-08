
class DesEngStudent:
    def __init__(self, name, year, budget):
        self.name = name
        self.year = year
        self.budget = budget
    
    def print(self):
        return "{} (DE{}) with £{} remaining".format(self.name, self.year, self.budget)

    def spend(self, value_spent):
        self.budget -= value_spent
        if self.budget < 0:
            raise ValueError
        return self.budget

    def three_d(self, quantity):
        return self.spend(quantity*5.50)

    def laser_cut(self, quantity):
        return self.spend(quantity*1)
    
    def paper_print(self, quantity):
        return self.spend(quantity*0.1)
