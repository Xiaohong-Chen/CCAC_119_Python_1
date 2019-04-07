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

class ProductionWorker(Employee):

    def __init__(self,employeeName,employeeNumber,shiftNumber,hourlyPayRate):
        Employee.__init__(self,employeeName,employeeNumber)
        self.__shiftNumber=shiftNumber
        self.__hourlyPayRate=hourlyPayRate

    def set_shiftNumber(self,shiftNumber):
        self.__shiftNumber=shiftNumber

    def get_shiftNumber(self):
        return self.__shiftNumber

    def set_hourlyPayRate(self,hourlyPayRate):
        self.__hourlyPayRate=hourlyPayRate

    def get_hourlyPayRate(self):
        return self.__hourlyPayRate

def main():
        print("Input following information of the productionWorker")
        employeeName=input("Enter Name:")
        employeeNumber=input("Enter Number:")
        shiftNumber=input("Enter Shift Number:")
        hourlyPayRate=input("Enter Hourly Pay Rate:")

        productionWorker = ProductionWorker(employeeName,employeeNumber,shiftNumber,hourlyPayRate)

        print("Information of the productionWorker")
        print("Employee name: ",productionWorker.get_employeeName())
        print("Employee number: ",productionWorker.get_employeeNumber())
        print("Shift number: ",productionWorker.get_shiftNumber())
        print("Hourly pay rate: ",productionWorker.get_hourlyPayRate())

main()