class Employee:
    def employeeDetails(self): # referring to the object itself
        self.name = 'Mathew'
        print('Name = ', self.name)
        age = 30 
        print('Age = ', age)

    def printEmployeeDetails(self):
        print('Printing in another method')
        print('Name = ', self.name)
        print('Age = ', age) # the lifespan of the attribute is only within the method

employee = Employee()
employee.employeeDetails()
# Employee.employeeDetails(employee)
employee.printEmployeeDetails()