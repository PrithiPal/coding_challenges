import math
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.table={}

    def sumRange(self, i: int, j: int) -> int:
        
        if i==j : 
            return self.arr[i]
        
        if i < len(self.arr) : 
            
            mid = math.floor((i+j)/2 )
            
            
            if (i,mid) in self.table : 
                first = self.table[(i,mid)]
            else:
                first = self.sumRange(i,mid)
                self.table[(i,mid)] = first
                
            if (j,mid) in self.table : 
                second = self.table[(mid+1,j)]
            else:
                second = self.sumRange(mid+1,j)
                self.table[(mid+1,j)] = second 
                
            return first+second
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
