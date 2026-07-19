class Solution(object):
    def buildArray(self, nums):
        ans=[]*len(nums)

        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans  
        