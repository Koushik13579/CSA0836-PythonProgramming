n1=int(input("Enter lower limit:"))
n2=int(input("Enter upper limit:"))
print("Numbers divisible by 5 but not by 10 are:")
for num in range(n1,n2+1):
    if(num%5==0 and num%10!=0):
        print(num,end=",")
