
def optimized_bubble_sort(array):
    global iterations
    iterations = 0
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - 1):
            iterations += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:          
            break

array = [i for i in range(1, 20)]

optimized_bubble_sort(array)
print(iterations)

