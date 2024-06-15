class Employee:

    raise_amt = 1.04
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@genesis.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

emp_1 = Employee('feyi','awopetu', 50000)
emp_2 = Employee('hillary', 'user', 67000)

Employee.set_raise_amt(1.12)

print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(Employee.raise_amt)
#print(emp_1.__dict__)
