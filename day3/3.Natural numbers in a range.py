print("Enetr the limits:")
N=int(input("Enter lower limit:"))
M=int(input("Enter upper limit:"))
if(M<=0):
    print("There are no natural numbers between n and m.")
else:
    print("Natural numbers between N and M are:")
    for i in range(N+1,M):
        print(i,end=",")