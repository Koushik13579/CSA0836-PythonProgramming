print("Enter a number:")
num=int(input())
a,b=0,1
c=1
i=1
print(a,b,end=" ")
while(i<num-1):
    c=a+b
    i+=1
    print(c,end=" ")
    a = b
    b = c