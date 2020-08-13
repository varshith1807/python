num=int(input("enter the value"))
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
result=factorial(num)
print("the factorial of",num,'is',result)

