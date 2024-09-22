def largest_span(arr, n):
    first_occurrence = {}
    max_span = 0
    
    for i in range(n):
        # If the value is not in the dictionary, store its first occurrence
        if arr[i] not in first_occurrence:
            first_occurrence[arr[i]] = i
        # Calculate the span and update the maximum span
        span = i - first_occurrence[arr[i]] + 1
        max_span = max(max_span, span)
    
    return max_span

# Input
n = int(input())  # Number of elements
arr = list(map(int, input().split()))  # Array elements

# Output the largest span
print(largest_span(arr, n))
