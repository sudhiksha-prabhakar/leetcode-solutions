class Solution(object):
    def singleNumber(self, nums):
        dupli={}

        for num in nums:
            if num in dupli:
                dupli[num]+=1
            else:
                dupli[num]=1

        for num in nums:
            if dupli[num]==1:
                return num            

                
        