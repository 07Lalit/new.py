def MaxSum(arr, windowsize, n):
    if n <= windowsize:
        print("Invalid operation")
        return -1
    k = [arr[i] for i in range(0, windowsize)]
    win_sum = sum(k)
    max_sum = win_sum

    for i in range(n - windowsize):
        win_sum = win_sum - arr[i] + arr[i + windowsize]
        max_sum = max(win_sum, max_sum)

    return max_sum


n = int(input("Enter a size of array : "))
m = int(input("Enter the window size : "))
arr = [int(i) for i in input("enter elements in array : ").split()]
ans = MaxSum(arr, m, n)
print(ans)