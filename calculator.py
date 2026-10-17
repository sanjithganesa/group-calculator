CONTRIBUTORS = ["Adam", "Sanjith","Gijendra Pugalenthi"]

def add(a, b):
    pass


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise Exception("Division by zero")
    return a / b


if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print(subtract(5, 3))
    print(divide(5,0))
    print(multiply(2,3))