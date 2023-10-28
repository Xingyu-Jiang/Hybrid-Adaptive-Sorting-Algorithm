import random
import time


# Insertion Sort
def insertion_sort_for_hybrid(arr: list, low: int, high: int) -> None:
    # Iterate through the subarray between indices 'low' and 'high'
    for i in range(low + 1, high + 1):
        key = arr[i]  # Current element to be inserted into the sorted subarray
        j = i - 1  # Start from the previous element

        # Compare 'key' with elements in the sorted subarray and shift them to the right if needed
        while j >= low and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1
        arr[j + 1] = key  # Insert 'key' into its correct position in the sorted subarray


# Partition function for Quick Sort
def partition(array: list, low: int, high: int) -> int:
    # Select a random index as the pivot element
    random_index = random.randint(low, high)
    pivot = array[random_index]

    # Swap the pivot element to the end of the subarray
    array[random_index], array[high] = array[high], array[random_index]

    i = low - 1  # Initialize an index for the smaller elements

    # Iterate through the subarray to partition it around the pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            # Swap the current element with the element at index 'i'
            array[i], array[j] = array[j], array[i]

    # Move the pivot element to its correct position in the sorted subarray
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1  # Return the index of the pivot element in its sorted position


# Hybrid Sort
def hybrid_sort(array: list, low: int, high: int, depth_limit: int) -> None:
    # Define what is small size
    small_size = 1_000
    # Check if there's more than one element in the subarray
    if low < high:
        # Check if the subarray is small (less than 10 elements) and the recursion depth limit is reached
        if high - low < small_size and depth_limit == 0:
            insertion_sort_for_hybrid(array, low, high)  # Use insertion sort for small subarrays
        else:
            # If the depth limit is reached, use Python's built-in sorted() function
            if depth_limit == 0:
                array[low:high + 1] = sorted(array[low:high + 1])
            else:
                pivot = partition(array, low, high)  # Use Quick Sort to partition the subarray
                # Recursively sort the two subarrays on each side of the pivot
                hybrid_sort(array, low, pivot - 1, depth_limit - 1)
                hybrid_sort(array, pivot + 1, high, depth_limit - 1)


# Convenience function to apply the hybrid sort
def apply_hybrid_sort(array: list) -> None:
    low = 0
    high = len(array) - 1
    depth_limit = 2 * int(high.bit_length())  # Calculate the depth limit based on the array size
    hybrid_sort(array, low, high, depth_limit)  # Call the hybrid_sort function to start the sorting process


def quickSort(array: list, low: int, high: int) -> None:
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# Convenience function to apply the quick sort
def apply_quickSort(array: list) -> None:
    low = 0
    high = len(array) - 1
    quickSort(array, low, high)


def Insert_Sort(lst: list) -> None:
    # Iterate through the list starting from the second element.
    for i in range(1, len(lst)):
        curr = i
        curr_value = lst[i]

        # Swap elements to the left until the current value is in its correct sorted position.
        while curr > 0 and curr_value < lst[curr - 1]:
            lst[curr] = lst[curr - 1]
            curr -= 1
        lst[curr] = curr_value


def Select_Sort(lst: list) -> None:
    # Iterate through the list in reverse order.
    for i in range(len(lst) - 1, 0, -1):
        curr_max = 0
        # Iterate through the unsorted portion of the list to find the maximum element.
        for j in range(1, i + 1):
            if lst[curr_max] < lst[j]:
                curr_max = j

        # Swap the maximum element with the last unsorted element.
        lst[i], lst[curr_max] = lst[curr_max], lst[i]


# Define a function called Bubble_Sort that takes a list (lst) as an argument.
def Bubble_Sort(lst: list) -> None:
    # Iterate through the list in reverse order.
    for i in range(len(lst) - 1, 0, -1):
        # Iterate through the list from the beginning to the current end.
        for j in range(i):
            # Swap adjacent elements if they are out of order
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def merge(arr, left_half, right_half):
    i = j = k = 0

    # Merge the two sorted halves into the original array
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Check if any elements were left
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        merge(arr, left_half, right_half)  # Merge the sorted halves back together


def measure_execution_time(array: list, funtion) -> float:
    start_time = time.time()
    funtion(array)
    end_time = time.time()
    return end_time - start_time


def generate_random_list(size: int, lower: int, upper: int) -> list:
    generated_list = [random.randint(lower, upper) for _ in range(size)]
    return generated_list


if __name__ == "__main__":
    # Generate a random list and a sorted version for comparison
    testArray = generate_random_list(10_000, 0, 100_000)
    Hybrid_Array = testArray.copy()
    Quick_Array = testArray.copy()
    Insert_Array = testArray.copy()
    Selection_Array = testArray.copy()
    Bubble_Array = testArray.copy()
    Merge_Array = testArray.copy()
    Builtin_Array = testArray.copy()

    time_taken = measure_execution_time(Hybrid_Array, apply_hybrid_sort)
    print(f'Hybrid Sort Time Took: {time_taken}')

    time_taken = measure_execution_time(Quick_Array, apply_quickSort)
    print(f'Quick Sort Time Took: {time_taken}')

    time_taken = measure_execution_time(Insert_Array, Insert_Sort)
    print(f'Insertion Sort Time Took: {time_taken}')

    time_taken = measure_execution_time(Selection_Array, Select_Sort)
    print(f'Selection Sort Time Took: {time_taken}')

    time_taken = measure_execution_time(Bubble_Array, Bubble_Sort)
    print(f'Bubble Sort Time Took: {time_taken}')

    time_taken = measure_execution_time(Merge_Array, merge_sort)
    print(f'Merge Sort Time Took: {time_taken}')

    time_taken = measure_execution_time(Builtin_Array, sorted)
    print(f'Python Built-in Sort Time Took: {time_taken}')

