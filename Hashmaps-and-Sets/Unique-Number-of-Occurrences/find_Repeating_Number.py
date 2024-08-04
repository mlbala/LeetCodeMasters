from collections import Counter
from typing import List

class Solution:
    def find_Repeating_Numbers(self, arr: List[int]) -> List[int]:
        # Create a Counter object to count occurrences of each number
        counter = Counter(arr)
        
        # List to hold repeating numbers
        repeating_numbers = [num for num, count in counter.items() if count > 1]
        
        return repeating_numbers
    
    
sol = Solution()

# Example arrays
arr1 = [1, 2, 2, 1, 1, 3]
arr2 = [1, 2]
arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

print(sol.find_Repeating_Numbers(arr1))  # Output: [1, 2]
print(sol.find_Repeating_Numbers(arr2))  # Output: []
print(sol.find_Repeating_Numbers(arr3))  # Output: [-3, 0, 1]