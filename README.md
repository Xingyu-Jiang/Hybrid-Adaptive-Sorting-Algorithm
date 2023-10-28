# Hybrid and Adaptive Sorting Algorithms

## Project Goals

**Project Goals:**
- To develop a hybrid sorting algorithm that leverages the strengths of both insertion sort and quick sort.
- To benchmark the performance of the hybrid algorithm against traditional sorting methods.
- To analyze the algorithm's performance both numerically and theoretically.
- Gain an in-depth understanding of sorting algorithms and their complexities.
- Gain proficiency in algorithm design and implementation.
- Gain experience in performance analysis and benchmarking.
- Gain problem-solving and critical-thinking skills.

## Algorithm Description

### Hybrid Sorting Algorithm

The developed sorting algorithm is a hybrid approach that selects either Insertion Sort, Quick Sort, or Python's built-in sorting function based on the size of the subarray and the depth of recursion.

- **Insertion Sort:** If the subarray is small (less than 1,000 elements) and the depth limit is reached, Insertion Sort is applied with a time complexity of O(n^2).

- **Quick Sort:** For larger subarrays, Quick Sort is employed, which has an average time complexity of O(n*log(n)). The pivot is chosen at random, and elements are partitioned around the pivot.

- **Resorting Small Subarrays:** If the depth limit is reached and the subarray size is still substantial, the code resorts to Python's built-in sorted function with a time complexity of O(n*log(n)).

- **Recursive Depth Limit:** The depth limit is calculated as 2 * int(high.bit_length()), ensuring that the recursion depth remains manageable.

## Benchmarking Results

To evaluate the performance of the hybrid sorting algorithm, benchmarking tests using randomly generated datasets of various sizes were used. The hybrid algorithm was compared against the following traditional sorting methods: Quick Sort, Insertion Sort, Selection Sort, Bubble Sort, Merge Sort, and Python's built-in sorted function.

### Numerical Results

**Sorting Algorithm and Their Time Taken in Seconds**

| Array size            | 1,000     | 10,000    | 20,000    |
|-----------------------|-----------|-----------|-----------|
| Hybrid Sort           | 1.00E-03  | 1.90E-02  | 4.54E-02  |
| Quick Sort            | 2.00E-03  | 1.99E-02  | 4.53E-02  |
| Insertion Sort        | 3.03E-02  | 3.27E+00  | 1.37E+01  |
| Selection Sort        | 1.89E-02  | 2.13E+00  | 9.63E+00  |
| Bubble Sort           | 5.30E-02  | 5.79E+00  | 2.34E+01  |
| Merge Sort            | 2.00E-03  | 2.60E-02  | 5.80E-02  |
| Built-in Sort Function| 1.02E-03  | 1.00E-03  | 3.00E-03  |

## Discussion

The hybrid sorting function was able to meet the expectation of being able to adapt to changes in the sample size. When the sample size was small enough, the hybrid sort was faster than Quick Sort, although it was unexpected that it was faster than Insertion Sort.

The theoretical analysis supported the observed performance, confirming that the algorithm's expected time complexity was O(n*log(n)) in most cases.

The use of Insertion Sort for small subarrays and the depth limit mechanism ensured that the algorithm avoided excessive overhead from recursion, contributing to its efficiency.

When the sample size exceeded 20,000, the system couldn't respond due to taking a long time performing Insertion Sort, Selection Sort, and Bubble Sort.

## Theoretical Analysis

The main concept this hybrid sorting algorithm is built upon is having the program perform Insertion Sort when the sample size is small enough, while having Quick Sort algorithm take care of the sorting when the sample size becomes too large.

In the best case, the time complexity of this algorithm should approach O(n) when the sample size is small and can be sorted efficiently with Insertion Sort. In the worst case, the time complexity should approach O(n*log(n)) when Quick Sort is used for large samples.

## Conclusion

The development and evaluation of the hybrid sorting algorithm exemplify the potential of amalgamating multiple algorithms to create a more efficient solution for tackling sorting challenges. The hybrid sorting algorithm developed here effectively leverages the strengths of both Insertion Sort and Quick Sort, resulting in a more powerful and high-performing sorting function. Additionally, it demonstrated its ability to adapt to changes in the sample size and outperform a few other traditional sorting algorithms, regardless of how small or large the sample size is.

Overall, this project not only yielded a functional sorting algorithm but also enriched my understanding of different sorting algorithms and their complexities. It enabled me to gain valuable experience in algorithm design, implementation, and performance analysis. Most importantly, it strengthened my problem-solving and critical-thinking skills.
