n=int(input("Enter a number:"))
num,count=n,0
while num!=0:
    num//=10
    count+=1
num,sum=n,0
while num!=0:
    rem=num%10
    sum+=rem**count
    num//=10
if(sum==n):
    print(n,"is an armstrong number.")
else:
    print(n,"is not an armstrong number.")