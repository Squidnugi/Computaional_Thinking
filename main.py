# Python3 program to sort an array
# using bucket sort
import sys
import time
import csv
import random


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])

    return merge(left_list, right_list)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Merge smaller elements first
    while left_list_index < len(left_list) and right_list_index < len(right_list):
        if left_list[left_list_index] <= right_list[right_list_index]:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
        else:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

    # If left list has more items, append them to sorted list
    while left_list_index < len(left_list):
        sorted_list.append(left_list[left_list_index])
        left_list_index += 1

    # If right list has more items, append them to sorted list
    while right_list_index < len(right_list):
        sorted_list.append(right_list[right_list_index])
        right_list_index += 1

    return sorted_list

def bucket_sort(arr):
    # 1. Create empty buckets
    buckets = [[] for _ in range(len(arr))]
    
    # 2. Insert elements into their respective buckets
    for num in arr:
        index_b = int(num * len(buckets))
        buckets[index_b].append(num)
    
    # 3. Sort each bucket individually
    for bucket in buckets:
        bucket.sort()
    
    # 4. Concatenate all buckets into arr
    i = 0
    for bucket in buckets:
        for num in bucket:
            arr[i] = num
            i += 1


#https://www.programiz.com/dsa/linear-search
def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

#https://www.programiz.com/dsa/binary-search
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2
        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

# Driver Code

def do_merge(array):
  merge_start_time = time.time()
  merge = merge_sort(starting_array)
  merge_end_time = time.time()
  return merge, merge_start_time, merge_end_time

def do_bucket(array):
    bucket_start_time = time.time()
    print(starting_array)
    bucket = bucketSort(array)
    
    print("Sorted Array in descending order is")
    print(bucket)
    bucket_end_time = time.time()
    return bucket, bucket_start_time, bucket_end_time

def do_linear(array):
    linear_start_time = time.time()
    x = 1
    n = len(array)
    result = linearSearch(array, n, x)
    if (result == -1):
        print("Element not found")
    else:
        print("Element found at index: ", result)
    linear_end_time = time.time()
    return result, linear_start_time, linear_end_time

def do_binary(array):
    binary_start_time = time.time()
    x = 4

    result = binarySearch(array, x, 0, len(array) - 1)

    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Not found")
    binary_end_time = time.time()
    return result, binary_start_time, binary_end_time

if __name__ == '__main__':
    starting_array = []
    filename = "large_file.csv"
  # Define the number of rows and columns you want in your CSV file
    num_rows = 100
    num_cols = 1
    # Open the file in write mode
    with open(filename, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)

    # Write the header (optional)
      #header = [f"Column{i+1}" for i in range(num_cols)]
      #writer.writerow(header)

    # Write the data rows
      for _ in range(num_rows):
        row = [random.randint(0, 100) for _ in range(num_cols)]
        writer.writerow(row)

    print(f"Created a CSV file '{filename}' with {num_rows} rows and {num_cols} columns.")
    with open(filename, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for i in reader:
        starting_array.append(int(i[0]))
    print(starting_array)
    #merge sort
    output = do_merge(starting_array)
    #bucket Sort
    #output = do_bucket(starting_array)
    #binary Search
    #output = do_binary(output[0])
    #linear Search
    #output = do_linear(output)
    print(output)
    print(f"Time: {(output[2] - output[1]) * 1000}ms")