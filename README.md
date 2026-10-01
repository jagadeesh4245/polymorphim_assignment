# Python Polymorphism Practice

A collection of 20 hands-on Python problems covering **polymorphism** in object-oriented programming: method overriding, duck typing, operator overloading, class methods, and polymorphic built-in functions.

All solutions live in a single file, [`polymorphism_problems.py`](./polymorphism_problems.py), and each problem prints its own output so you can run everything in one go.

## Table of Contents

- [Concepts Covered](#concepts-covered)
- [Problem List](#problem-list)
- [Getting Started](#getting-started)
- [Sample Output](#sample-output)
- [Key Takeaways](#key-takeaways)

## Concepts Covered

| Concept | Description | Problems |
|---|---|---|
| **Method overriding** | Child classes redefine a parent method with their own behavior | Q1, Q2, Q3, Q4, Q5, Q8, Q10, Q16, Q17, Q20 |
| **Duck typing** | Classes with no shared parent work with the same function as long as they have the same method | Q7, Q13, Q15, Q18 |
| **Method overloading (default args)** | One method handles a varying number of arguments | Q6 |
| **Operator overloading** | Custom behavior for `+` and `>` via `__add__`, `__gt__` | Q11, Q12, Q19 |
| **Built-in polymorphism** | `len()` and `type()` work across different data types | Q9 |
| **Class-level polymorphism** | `@classmethod` overridden in child classes | Q14 |

## Problem List

| # | Problem | What it demonstrates |
|---|---|---|
| 1 | Animal Sounds | Overriding `sound()` in `Dog`, `Cat`, `Cow` |
| 2 | Payment Methods | Overriding `pay()` for `UPI`, `CreditCard`, `Cash` |
| 3 | Employee Salary | Different salary logic for full-time vs part-time |
| 4 | Shape Area | `area()` for `Circle`, `Rectangle`, `Square` |
| 5 | Vehicle Information | `start()` for `Car`, `Bike`, `Bus` |
| 6 | Method Overloading | Default arguments in `Calculator.add()` |
| 7 | Notification (Duck Typing) | Email, SMS, WhatsApp sharing a `send()` method |
| 8 | Banking System | Interest rates for `SBI`, `HDFC`, `ICICI` |
| 9 | Built-in Functions | `len()` and `type()` on list, tuple, string, dict |
| 10 | Food Ordering | `prepare()` for `Pizza`, `Burger`, `Biryani` |
| 11 | Operator Overloading (`+`) | Adding two `Book` objects by page count |
| 12 | Operator Overloading (`>`) | Comparing `Product` objects by price |
| 13 | Media Player (Duck Typing) | `Audio`, `Video`, `Podcast` with `play()` |
| 14 | Class Methods | Overriding `@classmethod` in child classes |
| 15 | Shopping Cart | Category-based discounts via duck typing |
| 16 | Ride Booking | Fare calculation with parameters |
| 17 | Hospital Management | Specialist-specific `treat_patient()` |
| 18 | File Processing | `read_file()` for CSV, JSON, text |
| 19 | Custom Data Types | `Distance` class with `__add__` and `__str__` |
| 20 | Complete Challenge | Full employee hierarchy: `work()`, `calculate_bonus()`, `display_details()` |

## Getting Started

### Prerequisites

- Python 3.6+ (uses f-strings)

### Run

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python polymorphism_problems.py
```

No external libraries are needed (only the built-in `math` module).

## Sample Output

```text
--- Q1 ---
Dog barks
Cat meows
Cow moos

--- Q4 ---
Circle area: 153.94
Rectangle area: 20
Square area: 36

--- Q11 ---
Book 1 pages: 150
Book 2 pages: 200
Total pages: 350

--- Q16 ---
BikeRide fare for 10 km: Rs.80
CarRide fare for 10 km: Rs.150
AutoRide fare for 10 km: Rs.120

--- Q19 ---
Distance 1: 2 km 500 meters
Distance 2: 3 km 800 meters
Total: 6 km 300 meters
```

## Key Takeaways

- **Overriding** lets a single method name (`sound()`, `pay()`, `area()`) behave differently depending on the object's class.
- **Duck typing** means Python cares about *what an object can do*, not *what it inherits from*. If it has `send()`, it can be passed to `notify_user()`.
- **Python has no true method overloading**, so default arguments (`c=0`) are the common substitute.
- **Dunder methods** (`__add__`, `__gt__`, `__str__`) let your own classes work naturally with operators and `print()`.
- **`cls` in a class method** refers to the class it was called on, so polymorphism works without creating an object.

## License

This project is open source and available for learning and practice.
