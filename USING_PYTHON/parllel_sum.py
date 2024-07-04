def ParallelSum(arr):
    total_sum = sum(arr)
    
    if total_sum % 2 != 0:
        return -1

    target_sum = total_sum // 2
    current_sum = 0
    first_set = []

    for num in sorted(arr, reverse=True):
        if current_sum + num <= target_sum:
            first_set.append(num)
            current_sum += num

    if current_sum == target_sum:
        second_set = sorted(list(set(arr) - set(first_set)))
        result = ','.join(map(str, first_set + second_set))
        return result
    else:
        return -1

# Example usage:
x=[int(x) for x in input('enter no.').split()]
result = ParallelSum(x)
print(result)

# list(map(int,input('enter no.').split()))
