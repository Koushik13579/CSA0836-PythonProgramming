a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if (a>b):
    if(a>c):
        print("a=",a,"is the greatest number.")
    else:
        print("c=",c,"is the greatest number.")
else:
    if(b>c):
        print("b=",b,"is the greatest number.")
    else:
        print("c=",c,"is the greatest number.")