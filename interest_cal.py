
n =int(input("Enter the priciple amount : "))
m = float(input("Enter the instrest percentage : "))/100

for i in range(10):
    n  += (n*m)
    print("Year", i+1, "is", round(n,2))
