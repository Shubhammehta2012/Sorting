
# coding: utf-8

# # Bubble Sort

# In[2]:


# optimized bubble sort does not increase or decrease asymtotic notations
# however number of iterations can be reduced to some extent
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
        # if no swapping is performed that means sorting is complete
        # hence break out of the loop
        if not swapped:          
            break


# In[3]:


# elements are already sorted
array = [i for i in range(1, 20)]

optimized_bubble_sort(array)
# 20 ALREADY sorted elements need 18 iterations approx = n
print(iterations)

