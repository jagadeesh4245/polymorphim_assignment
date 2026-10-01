# ---------------- Q1. Animal Sounds ----------------
print("--- Q1 ---")

class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
class Cow(Animal):
    def sound(self):
        print("Cow moos")

Animal1 = Dog()
Animal2 = Cat()
Animal3 = Cow()

Animal1.sound()  # Output: Dog barks
Animal2.sound()  # Output: Cat meows
Animal3.sound()  # Output: Cow moos

# ---------------- Q2. Payment Methods ----------------
print("--- Q2 ---")

class Payment:
    def pay(self):
        print("Processing payment")
class UPI(Payment):
    def pay(self):
        print("Payment through UPI")
class CreditCard(Payment):
    def pay(self):
        print("Payment through credit card")
class Cash(Payment):
    def pay(self):
        print("Payment through cash")

payment1 = UPI()
payment2 = CreditCard()
payment3 = Cash()

payment1.pay()  # Output: Payment through UPI
payment2.pay()  # Output: Payment through credit card
payment3.pay()  # Output: Payment through cash


# ---------------- Q3. Employee Salary ----------------
print("--- Q3 ---")

class Employee:
    def calculate_salary(self):
        print("Salary calculation not defined")

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hours, hourly_rate):
        self.name = name
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours * self.hourly_rate

emp1 = FullTimeEmployee("Ravi", 50000)
emp2 = PartTimeEmployee("Anu", 80, 300)

for emp in (emp1, emp2):
    print(f"{emp.name}'s salary: {emp.calculate_salary()}")

import math

# ---------------- Q4. Shape Area ----------------
print("--- Q4 ---")
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return round(math.pi * self.r ** 2, 2)

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l, self.b = l, b
    def area(self):
        return self.l * self.b

class Square(Shape):
    def __init__(self, s):
        self.s = s
    def area(self):
        return self.s ** 2

for shape in (Circle(7), Rectangle(4, 5), Square(6)):
    print(f"{type(shape).__name__} area: {shape.area()}")


# ---------------- Q5. Vehicle Information ----------------
print("\n--- Q5 ---")
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with a key/button ignition")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick/self-start")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with an air-brake release and ignition")

for v in (Car(), Bike(), Bus()):
    v.start()


# ---------------- Q6. Method Overloading (default args) ----------------
print("\n--- Q6 ---")
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))        # 15
print(calc.add(10, 20))       # 30
print(calc.add(10, 20, 30))   # 60


# ---------------- Q7. Duck Typing - Notification ----------------
print("\n--- Q7 ---")
class EmailNotification:
    def send(self):
        print("Sending Email notification")

class SMSNotification:
    def send(self):
        print("Sending SMS notification")

class WhatsAppNotification:
    def send(self):
        print("Sending WhatsApp notification")

def notify_user(notifier):
    notifier.send()

for n in (EmailNotification(), SMSNotification(), WhatsAppNotification()):
    notify_user(n)


# ---------------- Q8. Banking System ----------------
print("\n--- Q8 ---")
class Bank:
    def interest_rate(self):
        return 0

class SBI(Bank):
    def interest_rate(self):
        return 6.5

class HDFC(Bank):
    def interest_rate(self):
        return 7.0

class ICICI(Bank):
    def interest_rate(self):
        return 6.8

def show_rate(bank):
    print(f"{type(bank).__name__} interest rate: {bank.interest_rate()}%")

for b in (SBI(), HDFC(), ICICI()):
    show_rate(b)


# ---------------- Q9. Built-in functions ----------------
print("\n--- Q9 ---")
my_list = [1, 2, 3]
my_tuple = (4, 5, 6, 7)
my_string = "Python"
my_dict = {"a": 1, "b": 2}

for obj in (my_list, my_tuple, my_string, my_dict):
    print(f"{obj!r:25} len = {len(obj)}, type = {type(obj)}")

# Explanation: len() and type() are polymorphic. len() calls the object's own
# __len__() method, so it counts items in a list/tuple, characters in a string
# and keys in a dictionary. type() returns the class of whatever object it gets.
# One function name, different behaviour depending on the object passed in.


# ---------------- Q10. Food Ordering ----------------
print("\n--- Q10 ---")
class Food:
    def prepare(self):
        print("Preparing food")

class Pizza(Food):
    def prepare(self):
        print("Pizza: knead dough, add sauce and cheese, bake in oven")

class Burger(Food):
    def prepare(self):
        print("Burger: grill patty, add veggies, assemble in a bun")

class Biryani(Food):
    def prepare(self):
        print("Biryani: cook rice and masala with meat/veg, dum cook")

def make_food(food):
    food.prepare()

for f in (Pizza(), Burger(), Biryani()):
    make_food(f)


# ---------------- Q11. Operator Overloading - Addition ----------------
print("\n--- Q11 ---")
class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book(150)
book2 = Book(200)
print("Book 1 pages:", book1.pages)
print("Book 2 pages:", book2.pages)
print("Total pages:", book1 + book2)


# ---------------- Q12. Operator Overloading - Comparison ----------------
print("\n--- Q12 ---")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __gt__(self, other):
        return self.price > other.price

p1 = Product("Laptop", 55000)
p2 = Product("Phone", 30000)
if p1 > p2:
    print(f"{p1.name} has the higher price: {p1.price}")
else:
    print(f"{p2.name} has the higher price: {p2.price}")


# ---------------- Q13. Duck Typing - Media Player ----------------
print("\n--- Q13 ---")
class Audio:
    def play(self):
        print("Playing audio")

class Video:
    def play(self):
        print("Playing video")

class Podcast:
    def play(self):
        print("Playing podcast")

def play_media(media):
    media.play()

for m in (Audio(), Video(), Podcast()):
    play_media(m)


# ---------------- Q14. Class Methods ----------------
print("\n--- Q14 ---")
class Employee:
    @classmethod
    def company_info(cls):
        print(f"{cls.__name__}: Employee of TechCorp")

class Developer(Employee):
    @classmethod
    def company_info(cls):
        print(f"{cls.__name__}: Builds software at TechCorp")

class DataAnalyst(Employee):
    @classmethod
    def company_info(cls):
        print(f"{cls.__name__}: Analyzes data at TechCorp")

Developer.company_info()
DataAnalyst.company_info()
# Explanation: both child classes override company_info(). Calling it on
# Developer runs Developer's version, and on DataAnalyst runs DataAnalyst's
# version. cls refers to the class the method was called on, so no object
# needs to be created. That is polymorphism at the class level.


# ---------------- Q15. Shopping Cart ----------------
print("\n--- Q15 ---")
class Electronics:
    def __init__(self, price):
        self.price = price
    def calculate_discount(self):
        return self.price * 0.10

class Clothing:
    def __init__(self, price):
        self.price = price
    def calculate_discount(self):
        return self.price * 0.20

class Grocery:
    def __init__(self, price):
        self.price = price
    def calculate_discount(self):
        return self.price * 0.05

def show_final_price(item):
    discount = item.calculate_discount()
    print(f"{type(item).__name__}: price={item.price}, discount={discount}, final={item.price - discount}")

for item in (Electronics(10000), Clothing(2000), Grocery(500)):
    show_final_price(item)


# ---------------- Q16. Ride Booking ----------------
print("\n--- Q16 ---")
class Ride:
    def calculate_fare(self, distance):
        return 0

class BikeRide(Ride):
    def calculate_fare(self, distance):
        return distance * 8

class CarRide(Ride):
    def calculate_fare(self, distance):
        return distance * 15

class AutoRide(Ride):
    def calculate_fare(self, distance):
        return distance * 12

def show_fare(ride, distance):
    print(f"{type(ride).__name__} fare for {distance} km: Rs.{ride.calculate_fare(distance)}")

for r in (BikeRide(), CarRide(), AutoRide()):
    show_fare(r, 10)


# ---------------- Q17. Hospital Management ----------------
print("\n--- Q17 ---")
class Doctor:
    def treat_patient(self):
        print("Doctor treats the patient")

class Cardiologist(Doctor):
    def treat_patient(self):
        print("Cardiologist: treats heart conditions using ECG and medication")

class Dentist(Doctor):
    def treat_patient(self):
        print("Dentist: treats teeth and gums with fillings and cleaning")

class Neurologist(Doctor):
    def treat_patient(self):
        print("Neurologist: treats brain and nerve disorders using MRI and therapy")

for d in (Cardiologist(), Dentist(), Neurologist()):
    d.treat_patient()


# ---------------- Q18. File Processing ----------------
print("\n--- Q18 ---")
class CSVFile:
    def read_file(self):
        print("Reading CSV file: splitting rows by commas")

class JSONFile:
    def read_file(self):
        print("Reading JSON file: parsing key-value pairs")

class TextFile:
    def read_file(self):
        print("Reading text file: reading plain lines")

def process_file(file_obj):
    file_obj.read_file()

for fobj in (CSVFile(), JSONFile(), TextFile()):
    process_file(fobj)


# ---------------- Q19. Custom Data Types ----------------
print("\n--- Q19 ---")
class Distance:
    def __init__(self, km, meters):
        self.km = km
        self.meters = meters
    def __add__(self, other):
        total_meters = (self.km + other.km) * 1000 + self.meters + other.meters
        return Distance(total_meters // 1000, total_meters % 1000)
    def __str__(self):
        return f"{self.km} km {self.meters} meters"

d1 = Distance(2, 500)
d2 = Distance(3, 800)
print("Distance 1:", d1)
print("Distance 2:", d2)
print("Total:", d1 + d2)


# ---------------- Q20. Complete Polymorphism Challenge ----------------
print("\n--- Q20 ---")
class Employee20:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        print(f"{self.name} is working")
    def calculate_bonus(self):
        return 0
    def display_details(self):
        print(f"Role: {type(self).__name__}, Name: {self.name}, Salary: {self.salary}")

class Manager(Employee20):
    def work(self):
        print(f"{self.name} is managing the team")
    def calculate_bonus(self):
        return self.salary * 0.20

class Developer20(Employee20):
    def work(self):
        print(f"{self.name} is writing code")
    def calculate_bonus(self):
        return self.salary * 0.15

class Tester(Employee20):
    def work(self):
        print(f"{self.name} is testing the application")
    def calculate_bonus(self):
        return self.salary * 0.10

employees = [
    Manager("Arun", 90000),
    Developer20("Divya", 70000),
    Tester("Karthik", 50000),
]

for emp in employees:
    emp.display_details()
    emp.work()
    print("Bonus:", emp.calculate_bonus())
    print()