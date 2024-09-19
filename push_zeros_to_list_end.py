# Input
n = int(input())  
arr = list(map(int, input().split()))  


result = []


for num in arr:
    if num != 0:
        result.append(num)


zero_count = arr.count(0)


result.extend([0] * zero_count)


print(*result)
