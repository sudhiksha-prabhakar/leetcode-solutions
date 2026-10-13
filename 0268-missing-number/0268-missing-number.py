class Solution(object):
    def missingNumber(self, nums):
        num=sorted(nums)
        for i in range(len(num)):
            if i!=num[i]:
                return i
        return len(num)  
        