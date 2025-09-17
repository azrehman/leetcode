#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        compliments = {}

        for i, n in enumerate(nums):
            if target - n in compliments:
                return [compliments[target - n], i]
            compliments[n] = i
        return [-1, -1]







        
# @lc code=end

