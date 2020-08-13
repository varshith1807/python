num=int(input("enter any value"))
count=0
for i in range(2,num):
        if num%i==0:
            count+=1
if count==0:
    print("the given number is prime")
else:
    print("the number is not a prime")
