# Write a function to find the longest common prefix string amongst an array of 
# strings.

# If there is no common prefix, return an empty string "".

""" Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

""" Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
def longestCommonPrefix(strs: list[str]) -> str:
    if not strs: return ""
    if len(strs) == 1: return strs[0]
    strs.sort()
    p = ""
    for x, y in zip(strs[0], strs[-1]):
        if x == y: p+=x
        else: break
    return p

def longestCommonPrefix(strs: list[str]) -> str:
    for i in range(min(len(ele) for ele in strs)):
        if len(set([strs[x][i] for x in range(len(strs))])) > 1:
            return strs[0][:i+1]
    return ""

print(longestCommonPrefix(["aba", "a"]))