a=int(input("Enter lower limit:"))
b=int(input("Enter upper limit:"))
print("Non primes are: ")
for i in range(a+1,b):
    for j in range(2,i):
        if(i%j==0):
            print(i,end=" ")
            break