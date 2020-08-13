str=input("enter a string")
def palindrome(str):
    for i in range(0,int(len(str)/2)):
        if str[i]==str[len(str)-1-i]:
            print("string is palindrome")
        else:
            print("not palindrome")
palindrome(str);
