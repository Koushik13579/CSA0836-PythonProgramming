limit = int(input("Enter upper limit: "))

for a in range(1, limit + 1):
    for b in range(a, limit + 1):
        c = (a**2 + b**2) ** 0.5
        if c.is_integer() and c <= limit:
            print(a, b, int(c))
