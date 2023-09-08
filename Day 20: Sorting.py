# Write your code here
    number_swaps = 0
    for _ in range(n):
        for index in range(n-1):
            if a[index] > a[index+1]:
                a[index], a[index+1] = a[index+1] , a[index]
                number_swaps+=1
    print("Array is sorted in",number_swaps, "swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
