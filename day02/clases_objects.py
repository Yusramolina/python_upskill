"""
in Java

class Item{

    String itemName;
    double itemPrice;

    static String madeItem = "china"

    Item(String itemName, double itemPrice){
        this.itemName = itemName;
        this.itemPrice = itemPrice;

    }

}

"""

class Item:
    made_in = 'China'  # static variable
    tariffs = "100%"  # static variable

    def __init__(self, item_name, item_price):
        self.item_name = item_name  # instance variable
        self.item_price = item_price  # instance variable

    def __str__(self):  # instance method
        return f'{type(self).__name__} {self.__dict__}'

    def instance_method(self):
        print(f"This is an instance method {self.item_name}")

    @staticmethod  # can not interact with any instance or static variables
    def static_method():
        print(f"This is a static method")

    @classmethod  # equivilent to static method of java: only accept static variables
    def class_method(cls):
        print(f"This is a class method: {cls.made_in}")


item1 = Item("Pen", 2)
item2 = Item("Book", 3)

print(item1)
print(item2)

print(Item.made_in)
print(Item.tariffs)

Item.class_method()
Item.static_method()

"""
Create Employee class:
    instance variables: employee_name, job_title, salary
    static_variables: pay_tax

    instance methods: 
        __init()__: declares and initalizes all the instance variables
        __str()__: creates string version of the object
        work(): displaye  ${employee_name} is working

    class method:
        display_employee_tax_rate()


"""
class Employee:

    pay_tax = 0.20  # Variable estática

    def __init__(self, employee_name, job_title, salary):
        self.employee_name = employee_name
        self.job_title = job_title
        self.salary = salary

    def __str__(self):
        return f'Employee: {self.employee_name}, Job Title: {self.job_title}, Salary: ${self.salary}'

    def work(self):
        print(f"{self.employee_name} is working.")

    @staticmethod
    def display_employee_tax_rate():
        print(f"La tasa de impuesto actual es del {Employee.pay_tax * 100}%")


# Ejemplo de uso:
emp1 = Employee("Yusra", "QA Engineer", 30000)
print(emp1)
emp1.work()
Employee.display_employee_tax_rate()








