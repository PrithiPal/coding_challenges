





def maxSum(arr,subset,ind) : 
    
    
    current_sum = sum(subset)
    
    if ind >= len(arr)-1 : 
        
        return current_sum     

     
    
    for i in range(ind+2,len(arr)) :  
        
        
        subset.append(arr[i])
        
        partial_sum = maxSum(arr,subset,i)
        
        
        if partial_sum > current_sum : 
            current_sum = partial_sum 
            
        subset.pop()
    
        
    return current_sum 
            
    
    
def maxSumCaller(arr) : 
    
    max_sum=0
    
    
    for i in range(len(arr)) : 
        partial_sum = maxSum(arr,[arr[i]],i)
        #print(partial_sum)
        if partial_sum > max_sum : 
            max_sum = partial_sum
            
    return max_sum
    
    
print("answer= ",maxSumCaller([3,7,4,6,5]))
