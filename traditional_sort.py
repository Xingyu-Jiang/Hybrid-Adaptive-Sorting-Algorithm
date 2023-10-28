import random
import time


def partition(array: list, low: int, high: int) -> int:
    random_index = random.randint(low, high)
    pivot = array[random_index]
    array[random_index], array[high] = array[high], array[random_index]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSort(array: list, low: int, high: int) -> None:
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


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


def measure_execution_time(array, algorithm):
    start_time = time.time()
    algorithm(array)
    end_time = time.time()
    return end_time - start_time


def generate_random_list(size: int, lower: int, upper: int) -> list:
    generated_list = [random.randint(lower, upper) for _ in range(size)]
    return generated_list


if __name__ == "__main__":
    testArray = generate_random_list(10_000, 0, 20_000)
    data_quick_sort = testArray.copy()
    data_insertion_sort = testArray.copy()

    time_taken = measure_execution_time(data_quick_sort, apply_quickSort)

    print(f'Quick Sort time Took: {time_taken}')

    time_taken = measure_execution_time(data_insertion_sort, Insert_Sort)

    print(f'Insertion Sort time Took: {time_taken}')
