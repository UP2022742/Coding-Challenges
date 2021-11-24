# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For 
# example, 121 is palindrome while 123 is not.

""" Example 1:
Input: x = 121
Output: true
"""
""" Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""

""" Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

""" Example 4:
Input: x = -101
Output: false
"""

class Solution:

    @staticmethod
    def isPalindrome_second(x: int) -> bool:

        # If when the int is converted into a string and reversed using slices
        # it's the same value, return palindrome.
        return False if x < 0 else x == int(str(x)[::-1])

print(Solution.isPalindrome_second(1122211))