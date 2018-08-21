

# # Insertion Sort
def insertion_sort(array):
    global iterations
    iterations = 0
    for i in range(1, len(array)):
        current_value = array[i]
        for j in range(i - 1, -1, -1):
            iterations += 1
            if array[j] > current_value:
                array[j], array[j + 1] = array[j + 1], array[j] 
            else:
                array[j + 1] = current_value
                break


array = [i for i in range(1, 20)]

insertion_sort(array)
print(array)
print(iterations)

