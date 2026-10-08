class Solution(object):
    def majorityElement(self, nums):
        maj={}
        for num in nums:
            if num not in maj:
                maj[num]=1
            else:
                maj[num]+=1    
            if maj[num]>len(nums)//2:
                return num    
        