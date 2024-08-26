num=int(input("Enter a number:"))
n,rev=num,0
while num!=0:
    rem=num%10
    rev=(rev*10)+rem
    num//=10
if(n==rev):
    print(n,"is a palindrome number.")
else:
    print(n,"is not a palindrome number.")