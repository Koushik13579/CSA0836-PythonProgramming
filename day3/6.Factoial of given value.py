def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
num=3
print("Factorial of",num,"=",fact(num))