import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f"{self.street_address}, Suite #{self.suite}, {self.city}"


class Employee:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    # Future objects will have different Employee's name
    # and Address's suite, the other attributes don't change
    # As prototypes:
    # - Not initial data for the Employee's name is given
    # - Suite is initialized as 0 as we don't know it's value
    main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
    aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )


# Without the EmployeeFactory, we must initialize the classes and
# use deepcopy.

main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

john = copy.deepcopy(main_office_employee)
john.name = "John"
john.address.suite = 101
jane = copy.deepcopy(aux_office_employee)
jane.name = "Jane"
jane.address.suite = 200

print("Without factory")
print(john)
print(jane)

# With factory. Just one line of code per employee

john = EmployeeFactory.new_main_office_employee("Jonh", 101)
jane = EmployeeFactory.new_aux_office_employee("Jane", 200)
print("With factory")
print(john)
print(jane)

