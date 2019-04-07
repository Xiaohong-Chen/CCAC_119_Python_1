class Employee:

    def __init__(self,employeeName,employeeNumber):
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber

    def set_employeeName(self,employeeName):
        self.__employeeName = employeeName

    def set_employeeNumber(self,employeeNumber):
        self.__employeeNumber = employeeNumber

    def get_employeeName(self):
        return self.__employeeName

    def get_employeeNumber(self):
        return self.__employeeNumber

class  ShiftSupervisor(Employee):

    def __init__(self,employeeName,employeeNumber,annualSalary,annualBonus):
        Employee.__init__(self,employeeName,employeeNumber)
        self.__annualSalary=annualSalary
        self.__annualBonus=annualBonus

    def set_annualSalary(self,annualSalary):
        self.__annualSalary=annualSalary

    def get_annualSalary(self):
        return self.__annualSalary

    def set_annualBonus(self,annualBonus):
        self.__annualBonus=annualBonus

    def get_annualBonus(self):
        return self.__annualBonus

def main():
        print("Input following information of the ShiftSupervisor")
        employeeName=input("Enter Name:")
        employeeNumber=input("Enter Number:")
        annualSalary=input("Enter Annual Salary:")
        annualBonus=input("Enter Annual Bonus:")

        shiftSupervisor = ShiftSupervisor(employeeName,employeeNumber,annualSalary,annualBonus)

        print("Information of the ShiftSupervisor")
        print("Employee name: ",shiftSupervisor.get_employeeName())
        print("Employee number: ",shiftSupervisor.get_employeeNumber())
        print("Annual Salary: ",shiftSupervisor.get_annualSalary())
        print("Annual Bonus: ",shiftSupervisor.get_annualBonus())

main()