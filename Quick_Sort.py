
# coding: utf-8

# # Quick Sort

# In[2]:


def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        temp = partition(array, low, high)
        
        quick_sort(array, low, temp - 1)
        quick_sort(array, temp + 1, high)


# In[4]:


# elements are already sorted
array = [i for i in range(1, 20)]

print(array)
# 20 ALREADY sorted elements need 18 iterations approx = n
quick_sort(array, 0, len(array) - 1)

print(array)

