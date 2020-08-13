n=int(input("enter the number"))
def findpalin(n):
    x=n
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if(x==rev):
        print("the number is palindrome")
    else :
        print("not a palindrome")
findpalin(n);
      
