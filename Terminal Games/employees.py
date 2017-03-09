#employees.py
#Demonstrates inheritance and encapsulation.
#Run through another program it prints employee name and hourly/wage pay
#Ryan LaRouche

class Employee():
    def __init__(self, name):
        self.__name = name

    def getName(self): #print name
        print(self.__name, end="")

    def setName(self, name):
        self.__name = name

class SalariedEmployee(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)
        self.__salary = 0

    def giveRaise(self, percent): #increase salary by (input/100)
        self.__salary += (self.__salary * (percent/100))

    def calculatePay(self, time): #calculate pay
        outcome = "$" + str(int((self.__salary/52)*time))
        return(outcome)
            
    def setSalary(self, salary): #set salary
        self.__salary = salary

class ContractEmployee(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)
        self.__rate = 0

    def giveRaise(self, percent):#increase rate by (input/100)
        self.__rate += (self.__rate * (percent/100))

    def calculatePay(self, time): #calculate pay
        outcome = "$" + str(int(self.__rate*time))
        return(outcome)

    def setRate(self, rate): #set rate
        self.__rate = rate
