import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def power(self, x, y):
        return x ** y

    def logarithm(self, x, base):
        return math.log(x, base)

def main():
    calculator = Calculator()
    
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Logarithm")
        print("7. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            
            if choice != '6':
                num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print("Result: ", calculator.add(num1, num2))
            elif choice == '2':
                print("Result: ", calculator.subtract(num1, num2))
            elif choice == '3':
                print("Result: ", calculator.multiply(num1, num2))
            elif choice == '4':
                try:
                    print("Result: ", calculator.divide(num1, num2))
                except ValueError as e:
                    print(e)
            elif choice == '5':
                print("Result: ", calculator.power(num1, num2))
            elif choice == '6':
                base = float(input("Enter the base for logarithm: "))
                print("Result: ", calculator.logarithm(num1, base))
        elif choice == '7':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()