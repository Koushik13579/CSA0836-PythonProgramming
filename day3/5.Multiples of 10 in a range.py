n=int(input("Enter lower limit:"))
m=int(input("Enter lower limit:"))
print("Multiples of 10 are:")
for i in range(n+1,m):
    if(i%10==0):
        print(i,end=",")