class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        s1,s2=nums[0],nums[0]
        
        for i in range(len(nums))  : 
            
            if nums[i] > s1 : 
                s1 = nums[i]
                s2=s1
            
            elif s1+nums[i] > s1 : 
                s1=s1+nums[i]
                
                if s1 > s2 : 
                    s2=s1
                    
            print("{},{}".format(s1,s2))
            
            
            
        
            
        
                
            
