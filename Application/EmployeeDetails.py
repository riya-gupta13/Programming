from Employees import Employees


class Main:

    def AddEmployee(self):
        name = input("Enter you Name \n")
        age = input("Enter your age \n")
        id = input("Enter your employee Id \n")
        email = input("Enter your EmailId \n")
        emp = Employees(name, age, email)
        emp.employeeList.append(emp)

    def EditEmployee(self):
        name = input("Enter you Name \n")
        age = input("Enter your age \n")
        id = input("Enter your employee Id \n")
        email = input("Enter your EmailId \n")

    def Options(self):
        loop = True
        while loop:
            print(
                """Menu: \n 1: Add Employee \n 2: Edit Employee \n 3: Delete Employee \n 4: Display Employees \n 5: 
                Exit""")
            number = int(input("Enter your choice \n"))
            if number == 1:
                print("Add Employee")
                d = Main()
                d.AddEmployee()
                # loop = True
            elif number == 2:
                print("Edit Employee \n")
            elif number == 3:
                print("Delete Employee")
            elif number == 4:
                print("Display Employees")
                emp = Employees()
                emp.displayEmployees()
            else:
                loop = False


if __name__ == '__main__':
    d = Main()

    d.Options()
