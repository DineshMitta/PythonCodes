n = int(input())

arr = list(map(int, input().split()))

first_occurance = {}
max_span=0

for i in range(n):
    
    if arr[i] not in first_occurance:
        first_occurance[arr[i]] = i
    span = i - first_occurance[arr[i]] + 1
    max_span = max(max_span, span)
    


    
print(max_span)



