class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        table=[]
        for y in range(len(grid)) : 
            t=[]
            for x in range(len(grid[0])) : 
                t.append(0)
            
            table.append(t)
        print(table)
            
        
        
        return  self.minPathSumRecurse(grid,table,0,0)
        
    def minPathSumRecurse(self,grid,table,x,y) :
              
        if x==len(grid[0])-1 and y==len(grid)-1 : 
            
            return grid[y][x]
        
        
        first,second=0,0
        check=[]
        
        if x < len(grid[0])-1  : 
            
            if table[y][x+1]  :
                first = table[y][x+1]
            else: 
                first = self.minPathSumRecurse(grid,table,x+1,y)
                table[y][x+1] = first 
            
            check.append(first)
        
        if y < len(grid)-1 : 
            if table[y+1][x] : 
                second = table[y+1][x]
            else:
                second = self.minPathSumRecurse(grid,table,x,y+1)
                table[y+1][x] = second
                
            check.append(second)
        
        #print("({},{})".format(x,y))
        
        return grid[y][x] + min(check)
        
