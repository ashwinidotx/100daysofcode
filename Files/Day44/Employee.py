class Employee(dict):
    def __init__(self): 
        self = dict() 

    def addInfo(self, name, salary): 
        self[name] = salary 



class EmpDetails:

    def AddEmp(self,name,salary):
        objE = Employee()
        objE.addInfo(name,salary)

    def printAll(self):
        obj = Employee() # to print.
        print(obj)
    
    def printSalary(self,name):
        objSalary = Employee()
        for temp in objSalary:
            if temp[name]==name:
                print(temp)

    
E = EmpDetails()
E.AddEmp("Ashwini",25000)
E.AddEmp("Abinash",45000)
E.AddEmp("Abheesta",3000000)
E.AddEmp("Aditya",25000)

E.printAll()
