# less efficient O(n^2 solution)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                return None
'''
# more efficient O(n) solution using hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate(nums):
            if num in complements:
                return [complements[num], i]
            else:
                complements[target - num] = i
        return None



