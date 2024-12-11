
class Solutions:
    def containsDuplicate(self, nums:list[int]) -> bool:
        # Initialize an empty set to keep track of unique numbers
        s = set()
        # Iterate through each number in the input list
        for x in nums:
            # Check if the number has already been encountered
            if x in s:
                # If it is in the set, we found a duplicate, so return True
                return True
            else:
                s.add(x)

        return False
                


# Test case 1: Array with duplicates
nums = [1, 2, 3, 4, 1]
# Expected output: True
print(Solutions().containsDuplicate(nums))

# Test case 2: Array with all unique elements
nums = [1, 2, 3, 4, 5]
# Expected output: False
print(Solutions().containsDuplicate(nums))

# Test case 3: Array with only one element
nums = [1]
# Expected output: False
print(Solutions().containsDuplicate(nums))

# Test case 4: Array with multiple duplicates
nums = [1, 1, 1, 1, 1]
# Expected output: True
print(Solutions().containsDuplicate(nums))

# Test case 5: Empty array
nums = []
# Expected output: False
print(Solutions().containsDuplicate(nums))

# Test case 6: Large array with no duplicates
nums = list(range(10000))  # Unique elements from 0 to 9999
# Expected output: False
print(Solutions().containsDuplicate(nums))

# Test case 7: Large array with duplicates
nums = list(range(9999)) + [5000]  # Duplicates the number 5000
# Expected output: True
print(Solutions().containsDuplicate(nums))
