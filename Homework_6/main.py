class Calculator:

    def add(self, a, b):
        "сложение двух чисел."
        return f"Сложение: {a} + {b} = {a + b}"

    def subtract(self, a, b):
        "вычитание"
        return f"Вычитание: {a} - {b} = {a - b}"

    def multiply(self, a, b):
        "умножение"
        return f"Умножение: {a} * {b} = {a * b}"

    def divide(self, a, b):
        "деление"
        if b == 0:
            return "Ошибка: деление на 0!"
        return f"Деление: {a} / {b} = {a / b}"

def menu():

    print("""Калькулятор:\n(для выхода напишите: 'end')""")

    while True:

        a = input("Введите 'a': ")
        if a == 'end':
            break
        b = input("Введите 'b': ")
        if b == 'end':
            break

        a = int(a)
        b = int(b)

        operation = input("Введите операцию (Сложение, Вычитание, Умножение, Деление): ")

        match operation:
            case "end":
                break
            case "Сложение":
                print(calculator.add(a, b))
            case "Вычитание":
                print(calculator.subtract(a, b))
            case "Умножение":
                print(calculator.multiply(a, b))
            case "Деление":
                print(calculator.divide(a, b))

calculator = Calculator()
menu()
