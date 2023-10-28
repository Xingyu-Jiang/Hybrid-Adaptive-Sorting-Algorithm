import random
import time


# Insertion Sort
def insertion_sort(arr: list, low: int, high: int) -> None:
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
            insertion_sort(array, low, high)  # Use insertion sort for small subarrays
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
    testArray = generate_random_list(100_000, 0, 20_000)
    sorted_testArray = sorted(testArray)

    # Measure the time it takes to sort the array using the hybrid sort
    time_taken = measure_execution_time(testArray, apply_hybrid_sort)
    print(f'Time Took: {time_taken}')

    # Check if the sorted array matches the sorted version of the original array
    if testArray == sorted_testArray:
        print("Sorted")
    else:
        print("Not sorted")
