def a(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    
    return sorted(str1) == sorted(str2)
    

str1 = input()
str2 = input()
if a(str1,str2) == True:
    print("Strings are anagrams of each other")
else:
    print("Strings are not anagrams of each other")