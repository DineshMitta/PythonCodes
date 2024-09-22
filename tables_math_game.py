
print("Math Game")

n = int(input("Enter your  multiples : "))
s = 0 
for i in range(1, 11):
    print(f" {n} x {i} = ", end=" ")
    m = int(input())

    if m == n*i :
        print("Great Work!!\n")
        s+=1
    else:
        print("Wrong better luck next time\n")

print("Score : ",s)