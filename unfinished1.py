

n = int(input())

arr = list(map(int, input().split()))
k=0
for i in range(n):
    if arr[i] == 0:
        if i+1 < len(arr):
            k = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = k
            if arr[-i] == 0:
                m = arr[-i]
                arr[-i] = arr[i]
                arr[i] = m
            
for i in range(n):
    print(arr[i],end=" ")