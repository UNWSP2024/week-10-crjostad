class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print()

def main():
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    print("Employee 1:")
    employee1.display_employee()

    print("Employee 2:")
    employee2.display_employee()

    print("Employee 3:")
    employee3.display_employee()

if __name__ == "__main__":
    main()

