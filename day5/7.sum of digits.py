n = int(input("Enter a number: "))

while n >= 10:
    n = sum(int(digit) for digit in str(n))

print("Single digit sum:", n)