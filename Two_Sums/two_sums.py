from typing import List

# More mathmatics, faster but uses more memory... but significatly faster.
def twoSum_one(nums: list[int], target: int) -> list[int]:
    values = {}
    for i, num in enumerate(nums):
        remaining = target - num
        if remaining in values:
            return [i, values[remaining]]
        else:
            values[num] = i

# Double loop, slow but uses less memory
def twoSum_two(nums: list[int], target: int) -> list[int]:
    for index1 in range(len(nums)):
        for index2 in range(len(nums)):
            if nums[index1] + nums[index2] == target and index1 != index2:
                return [index1, index2]

print(twoSum_one([3,5,7,1,2,3,4], 7))