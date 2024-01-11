#!/usr/bin/env python
# coding: utf-8

# In[46]:


#Merge Sort 

def MergeSort(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    MergeSort(left_half)
    MergeSort(right_half)
    merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

n = int(input("Please enter the size of the array: "))
my_arr = []

for u in range(n):
    inp = int(input("Enter a number: "))
    my_arr.append(inp)

MergeSort(my_arr)

if len(my_arr) <= 1:
    print("Array is too short to be sorted")
else:
    print("Sorted array:", my_arr)


# 
