print("Enter the principle amount:")
p=int(input())
print("Enter the time in years:")
t=int(input())
print("Enter the rate of interest:")
r=int(input())
si=(p*t*r)/100
ci=p*(1+r/100)**t-p
print("Simple interest: ",si)
print("Compound interest: ",ci)