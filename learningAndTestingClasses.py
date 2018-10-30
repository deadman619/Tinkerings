class Employee:
    
    raiseAmount = 1.04

    def __init__(self, firstName, lastName, pay):    #constructor(initialiser?)
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName+'.'+lastName+'@email.com'
        self.pay = pay

    # Alternative constructor (from string)
    @classmethod
    def fromString(cls,empStr):
        firstName, lastName, pay = empStr.split('-')
        return cls(firstName, lastName, pay)
    

    def fullName(self):
        return '{} {}' .format(self.firstName, self.lastName)

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def setRaiseAmount(cls,amount):
        cls.raiseAmount = amount

class Developer(Employee):     # subclass inherits from parent, but lets you change stuff

    raiseAmount = 1.10

    def __init__(self, firstName, lastName, pay, progLang):
        super().__init__(firstName,lastName,pay)      #take from parent
        self.progLang = progLang

    def specializedIn(self):
        return self.progLang

class Manager(Employee):

    def __init__(self, firstName, lastName, pay, employees = None):
        super().__init__(firstName, lastName, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print ("Already in employee list")

    def removeEmp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print ("No such employee exists")

    def printEmp(self):
        for emp in self.employees:
            print(emp.fullName())

# constructor examples

emp1 = Employee('John', 'Smith', 50000)
dev1 = Developer('Test', 'Dev', 60000, 'Java')
mgr1 = Manager('Big', 'Guy', 70000, [dev1])
mgr2 = Manager('Bat', 'Man', 30000)
empStr1 = 'John-Doe-70000'
strEmp = Employee.fromString(empStr1)

print (dev1.specializedIn())     # Two ways to call it
print (Developer.specializedIn(dev1))

print (Employee.fullName(strEmp), strEmp.email, strEmp.pay)

# function examples

Employee.setRaiseAmount(1.10)
Developer.setRaiseAmount(1.4)

print ('-' * 50)
mgr1.printEmp()
print ('-' * 50)
Manager.addEmp(mgr1, emp1)
Manager.addEmp(mgr1, strEmp)
mgr1.printEmp()
print ('-' * 50)

