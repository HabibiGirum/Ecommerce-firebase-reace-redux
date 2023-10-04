# python object-oriented programming


class Employee():
    def __init__(self,name,lastname,pay):
        self.name=name
        self.lastname=lastname
        self.pay=pay
        self.email=name+"."+lastname+"@gmail.com"
    def fullname(self):
        return '{} {}'.format(self.name,self.lastname)


emp_1 = Employee("Habtamu","Girum",5000)

print(emp_1.name)
print(emp_1.fullname())