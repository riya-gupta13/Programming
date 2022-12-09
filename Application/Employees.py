class Employees:
    # id = 1

    def __init__(self, name, age, email):
        id = 1
        self.name = name
        self.age = age
        self.Id = id + 1
        self.email = email
        self.employeeList = []

    def displayEmployees(self):
        for e in self.employeeList:
            print(e)
