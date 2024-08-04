#1207
from collections import Counter

class Solution:
    def is_Unique_Occurrences(self, arr: list[int]) -> bool:
        counter = Counter(arr)
        occurrences  =set()
        for count in counter.values():
            if count in occurrences :
                return False
            occurrences .add(count)
        return True
    

sol = Solution()

# Example arrays
arr1 = [1, 2, 2, 1, 1, 3]
arr2 = [1, 2]
arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

# Call the method and print the results
print(sol.is_Unique_Occurrences(arr1))  # Output: True
print(sol.is_Unique_Occurrences(arr2))  # Output: False
print(sol.is_Unique_Occurrences(arr3))  # Output: True