def ArrayRotation(arr):
    N = arr[0] % len(arr)  # Get the rotation index

    rotated_array = arr[N:] + arr[:N]  # Perform circular rotation

    result_string = ''.join(map(str, rotated_array))  # Convert the rotated array to a string

    return result_string

x=[int(x) for x in input('enter list.').split()]
result = ArrayRotation(x)
print(result)

