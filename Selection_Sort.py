
def selection_sort(array):
    global iterations
    iterations = 0
    for i in range(len(array)):
        minimum_index = i
        for j in range(i + 1, len(array)):
            iterations += 1
            if array[minimum_index] > array[j]:
                minimum_index = j
        
        if minimum_index != i:
            array[i], array[minimum_index] = array[minimum_index], array[i]


array = [i for i in range(20)]
selection_sort(array)

print(array)
print(iterations)

