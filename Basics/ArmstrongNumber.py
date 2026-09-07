n=int(input("Enter a number: "))

num=n
sum=0
count=0

while(num>0):
    num=num//10
    count+=1

num=n

while n>0:
    digit=n%10
    sum+=pow(digit,count)
    n//=10

if sum==num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")