def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if (y == 0):
        print("Division by zero error!")
    else:
        return x / y


print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("Enter the operation you want to perform as 1 or 2 or 3 or 4:")
option = input()
if option in ['1', '2', '3', '4']:
    print("Enter first number:")
    a = int(input())
    print("Enter second number:")
    b = int(input())
    if option == '1':
        print("Result=", add(a, b))
    elif option == '2':
        print("Result=", sub(a, b))
    elif option == '3':
        print("Result=", mul(a, b))
    elif option == '4':
        print("Result=", div(a, b))
else:
    print("Invalid option!")
