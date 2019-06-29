Emp = dict()

class EmpDetails:

    def AddEmp(self,name,salary):
        Emp[name] = salary

    def printAll(self):
        print(Emp)
    
    def printSalary(self,name):
        print(name, Emp[name])
    
    def printNames(self,salary):
        for names, sals in Emp.items():
          if sals>=salary:
            print(names)
        

    
E = EmpDetails()
E.AddEmp("Ashwini",25000)
E.AddEmp("Abinash",45000)
E.AddEmp("Abheesta",3000000)
E.AddEmp("Aditya",25000)



E.printAll()
E.printSalary("Ashwini")
E.printNames(45000)
