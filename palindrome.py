#to check weather a number is palindrome or not
num=int(input("enter the value"))
temp=num
rev=0
while(num!=0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print("the number is palindrome")
else:
    print("the number is not palindrome")
