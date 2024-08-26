def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num*fact(num-1)

n=int(input("Enter upper limit:"))
sum=0
for i in range(1,n+1):
    sum+=(fact(i))
print("Sum of factorials till",n,"=",sum)