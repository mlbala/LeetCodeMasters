# Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

### Example

**Example 1:**

- Input: `nums = [2,7,11,15]`, `target = 9`
- Output: `[0, 1]`
- Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

**Example 2:**

- Input: `nums = [3,2,4]`, `target = 6`
- Output: `[1, 2]`

**Example 3:**

- Input: `nums = [3,3]`, `target = 6`
- Output: `[0, 1]`

### Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

### Follow-up

Can you come up with an algorithm that is less than O(n^2) time complexity?



*Code Explanation*
**Function Definition**
- `class Solution`:Defines a class named `Solution`.
- `def twoSum(self, nums: List[int], target: int) -> List[int]`: Defines the method twoSum which takes:
-- `nums`: A list of integers (`List[int]`).
-- `target`: An integer representing the target sum we need to find.
-- Returns a list of integers (`List[int]`), which are the indices of the two numbers that add up to target.
**Initialize Dictionary**
- `num_to_index` = {}: Creates an empty dictionary called num_to_index to map numbers to their indices as we iterate through the list.
**Iterate Over List**
- `for index, num in enumerate(nums)`: Loops through the nums list, providing both the current index and number.
**Calculate Complement**
- `complement = target - num`: Computes the complement needed to reach the target by subtracting the current number from the target.
**Check for Complement**
- `if complement in num_to_index`: Checks if the complement exists in the num_to_index dictionary.
    - If the complement is found, it means the complement and the current number together sum up to the target. Thus, the indices of these two numbers are returned.
    - `return [num_to_index[complement], index]`: Returns the indices of the complement and the current number.
**Update Dictionary**
- `num_to_index[num] = index`: Adds the current number and its index to the dictionary. This helps in future checks if the complement for upcoming numbers is found.
**Return Empty List**
return []: Returns an empty list if no solution is found. According to the problem constraints, there will always be one valid answer, so this line is more of a safeguard.
**Complexity Analysis**
***Time Complexity***: O(n), where n is the number of elements in the array. The function makes a single pass through the list, and each dictionary operation (lookup and insertion) is O(1) on average.
- ***Space Complexity***: O(n), where n is the number of elements in the array. This space is used by the dictionary to store indices of numbers.
**Usage**
You can run the two_sum function with your input list and target value to get the indices of the two numbers that add up to the target.

Example
```python

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
```