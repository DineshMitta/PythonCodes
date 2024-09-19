

n = int(input())

arr = list(map(int, input().split()))

res = []

for n in arr:
    if n != 0:
        res.append(n)
    

zero_c = arr.count(0)

res.extend([0] * zero_c)

print(*res)