class Employee:

    def __init__(self, name):
        self.name = name # 1st name: attribute name # 2nd name: parameter name

    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee('Mark')
employeeTwo = Employee('Mathew')
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()