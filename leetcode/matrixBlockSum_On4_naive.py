class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        
        if mat==[] : 
            return []
        
        x_len = len(mat[0])
        y_len = len(mat)


        # memoize table
        table = []
        for y in range(y_len) :
            t=[]
            for x in range(x_len) : 
                t.append(0)
            table.append(t)



        for x in range(x_len) : 
            for y in range(y_len) :

                current = 0

                for i in range(x-K,x+K+1) : 
                    for j in range(y-K,y+K+1) : 

                        if i >=0 and j>=0 and i<=x_len-1 and j<=y_len-1 : 

                            current = current + mat[j][i]

                table[y][x] = current


        return table



            

            
                
                
          
