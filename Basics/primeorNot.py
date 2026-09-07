from numpy import sqrt

n=int(input("Enter a number: "))
count=0

for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        if i*i==n:
            count+=1
        else:
            count+=2

if count==2:
    print("Prime Number")   
else:
    print("Not a Prime Number")
