class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, a, b):
        self.result = a + b
        return self.result
    def sub(self, a, b):
        self.result = a - b
        return self.result
    def prod(self, a, b):
        self.result = a * b
        return self.result
    def quotient(self, a, b):
        try:
            self.result = a / b
            return self.result
        except ZeroDivisionError:
            return "Error! divide by zero"

class ScientificCalculator(Calculator):
    def power(self, a, b):
        self.result = a ** b
        return self.result
    def sqrt(self, a):
        self.result = a ** 0.5
        return self.result

sci_calc = ScientificCalculator()

while True:
    print("\n--- Scientific Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Product")
    print("4. Division")
    print("5. Power")
    print("6. Square root")
    print("7. Exit")
    
    c = int(input("Enter the choice: "))

    if c == 7:
        print("Exit")
        break

    if c >= 1 and c <= 5:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    elif c == 6:
        a = int(input("Enter number: "))
    else:
        print("Invalid choice")
        continue

    if c == 1:
        print("Result =", sci_calc.add(a, b))
    elif c == 2:
        print("Result =", sci_calc.sub(a, b))
    elif c == 3:
        print("Result =", sci_calc.prod(a, b))
    elif c == 4:
        print("Result =", sci_calc.quotient(a, b))
    elif c == 5:
        print("Result =", sci_calc.power(a, b))
    elif c == 6:
        print("Result =", sci_calc.sqrt(a))
