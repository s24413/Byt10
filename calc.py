from abc import ABC, abstractmethod

class OperationHandler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, operation, num1, num2):
        pass

class BaseMathHandler(OperationHandler):
    def handle_request(self, operation, num1, num2):
        if self.successor:
            return self.successor.handle_request(operation, num1, num2)
        else:
            return None

class AdditionHandler(BaseMathHandler):
    def handle_request(self, operation, num1, num2):
        if operation == '+':
            return num1 + num2
        else:
            return super().handle_request(operation, num1, num2)

class SubtractionHandler(BaseMathHandler):
    def handle_request(self, operation, num1, num2):
        if operation == '-':
            return num1 - num2
        else:
            return super().handle_request(operation, num1, num2)

class MultiplicationHandler(BaseMathHandler):
    def handle_request(self, operation, num1, num2):
        if operation == '*':
            return num1 * num2
        else:
            return super().handle_request(operation, num1, num2)

class DivisionHandler(BaseMathHandler):
    def handle_request(self, operation, num1, num2):
        if operation == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Cannot divide by zero!"
        else:
            return super().handle_request(operation, num1, num2)

class Calculator:
    def __init__(self):
        self.chain = AdditionHandler(SubtractionHandler(MultiplicationHandler(DivisionHandler())))

    def calculate(self, operation, num1, num2):
        return self.chain.handle_request(operation, num1, num2)

calculator = Calculator()

operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculator.calculate(operation, num1, num2)

print("Result:", result)
