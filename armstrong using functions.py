num=int(input("enter the value"))
def find(num):
    sum=0
    x=num
    while x>0:
        digit=x%10
        sum+=digit**3
        x//=10
    if num==sum:
        print("the number is armstrong")
    else:
        print("not armstrong")
find(num);
