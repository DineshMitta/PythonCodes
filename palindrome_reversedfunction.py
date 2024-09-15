str = input("Enter String : ")

str2 = "".join(reversed(str))

print(str2)
if str2 == str :
    print("Palindrome ")
elif str2 != str:
    print("Not Plaindrome")
else :
    print("invalid")