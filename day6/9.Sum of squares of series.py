ul=int(input("Enter upperlimit:"))
sum = sum(i**2 for i in range(1,ul+1))

print("Sum of squares till",ul,"is:",sum)