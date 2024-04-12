class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours() # access to the methods of the base class

employee = Employee()
employee.setNumberOfWorkingHours()
print('Number of working hours of employees:', end=' ')
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print('Number of working hours of trainees:', end=' ')
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print('Number of working hours of trainees after reset:', end=' ')
trainee.displayNumberOfWorkingHours()