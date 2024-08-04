from collections import Counter
from typing import List

class Solution:
    def find_Non_Repeating_Numbers(self, arr: List[int]) -> List[int]:
        """
        Given a list of integers `arr`, return a list of integers that appear exactly once in the list.

        Args:
        arr (List[int]): A list of integers.

        Returns:
        List[int]: A list of integers that appear exactly once in the input list.

        Example:
        >>> sol = Solution()
        >>> sol.find_Non_Repeating_Numbers([1, 2, 2, 3, 3, 4])
        [1, 4]
        """
        # Create a Counter object to count occurrences of each number
        counter = Counter(arr)
        
        # List to hold non-repeating numbers
        non_repeating_numbers = [num for num, count in counter.items() if count == 1]
        
        return non_repeating_numbers

# Instantiate the Solution class
sol = Solution()

# Example test cases
print(sol.find_Non_Repeating_Numbers([1, 2, 2, 3, 3, 4]))  # Output: [1, 4]
print(sol.find_Non_Repeating_Numbers([1, 1, 2, 2, 3, 4, 4, 5]))  # Output: [3, 5]
print(sol.find_Non_Repeating_Numbers([7, 8, 9, 7, 8]))  # Output: [9]
print(sol.find_Non_Repeating_Numbers([10]))  # Output: [10]
print(sol.find_Non_Repeating_Numbers([11,12,13,14,15]))  # Output: [11,12,13,14,15]
print(sol.find_Non_Repeating_Numbers([1, 2, 2, 3, 3, 4, 4, 5, 5, 6]))  # Output: [1, 6]
