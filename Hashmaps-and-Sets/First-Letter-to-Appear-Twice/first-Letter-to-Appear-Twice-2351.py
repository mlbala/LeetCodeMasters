from typing import List

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        """
        Given a string `s`, find the first letter to appear twice.

        Args:
        s (str): The input string containing lowercase English letters.

        Returns:
        str: The first letter that appears twice in the string.

        Example:
        >>> sol = Solution()
        >>> sol.repeatedCharacter("abacabad")
        'a'
        
        >>> sol.repeatedCharacter("abcdd")
        'd'
        """
        seen = set()
        
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        
        # According to the problem description, there will always be a repeating character.
        # Therefore, there is no need to handle cases where no repeat is found
    # Instantiate the Solution class
sol = Solution()
# Test cases
print(sol.repeatedCharacter("abacabad"))  # Output: "a"
print(sol.repeatedCharacter("abcdd"))     # Output: "d"
print(sol.repeatedCharacter("zyxwzyx"))   # Output: "z"
print(sol.repeatedCharacter("a"))         # Output: "a" (though it won't appear due to constraints)
