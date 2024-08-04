# 1207. Unique Number of Occurrences

**Difficulty:** Easy

## Problem Statement

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is unique or `false` otherwise.

### Examples

**Example 1:**

**Input:**
```python
arr = [1, 2, 2, 1, 1, 3]
```

# Detailed Explanation of the `is_Unique_Occurrences` Method

## Explanation

### Importing Modules

```python
from collections import Counter
```

```from collections import Counter```: Imports the Counter class from the collections module to facilitate counting elements.

## Creating the Counter Object

```counter = Counter(arr)```

```counter = Counter(arr)```: Counts the occurrences of each element in the list arr. The result is a dictionary-like object where keys are elements of arr and values are their counts.

## Tracking Occurrences

```occurrences = set()
```

```occurrences = set()```: Initializes an empty set to keep track of the counts seen so far.

## Checking for Unique Counts
* The for count in `counter.values()` loop iterates through the occurrence counts.
* If a count is already in the `occurrences` set, it means this count has appeared before, so the function returns False.
* If the count is not in the set, it is added to the set.

## Returning the Result
* If all counts are unique, the function returns `True`

``` # Instantiate the Solution class
sol = Solution()

# Example arrays
arr1 = [1, 2, 2, 1, 1, 3]
arr2 = [1, 2]
arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

# Call the method and print the results
print(sol.is_Unique_Occurrences(arr1))  # Output: True
print(sol.is_Unique_Occurrences(arr2))  # Output: False
print(sol.is_Unique_Occurrences(arr3))  # Output: True
```