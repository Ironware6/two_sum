#Two_Sum Solution LEETCODE by Rafael Perez
#Very Inefficient XD. 
#Runtime: 6844 ms, faster than 5.00% of Python online submissions for Two Sum.
#Memory Usage: 12.5 MB, less than 84.59% of Python online submissions for Two Sum.#

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if (nums[i] + nums[j]) == target and (i != j):
                    return(i,j)
