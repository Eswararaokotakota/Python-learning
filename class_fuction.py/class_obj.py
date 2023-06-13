

class office:
    def employes(self,job_role,salary,experiance):
        self.role = job_role
        self.amount= salary
        self.years = experiance
    
    def operators(eswar,age,experiance,salary): # no need to write self only youcan write what ever you want 
        eswar.age = age             #and need to call with the name you written here i used my name eswar as self
        eswar.amount =salary
        eswar.years = experiance
        eswar.role= "engineer"
    

class employee:
    def eswar(self,name,salary,age):
        self.name = name
        self.salary= salary
        self.age = age
    def rao(self,role):
        self.role= role  


class Employ:
    def __init__ (self, name, nation, pay, language):
        self.name = name
        self.nation = nation
        self.pay = pay
        self.language = language
        self.email = name + '@gmail.com'



if __name__=="__main__":
    offee = office()
    offee.employes("engineer",20000,"2years")
    print(offee.role,offee.amount)
    offee.operators(27,"4years",18000)
    print(offee.age,offee.amount,offee.role)

    e=employee()
    e.eswar("Eswar",20000,21)
    e.rao("engineer")
    print(e.age,e.role)
    
    emp_1 = Employ("Eswar","Indian",20000,"Telugu")
    emp_2 = Employ("Rao","Indian",30000,"English")
    emp_3 = Employ("Eswara Rao","Indian",40000,"Hindi")

    print(emp_1.email,emp_1.pay)
    print(emp_2.email,emp_1.nation)