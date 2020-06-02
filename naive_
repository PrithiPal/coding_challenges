def subset1(arr,r,i,subarray) : 
    
    ## base case here 
    print(subarray)
    c = 0 
    
    if len(subarray)==3 : 
        i = subarray[0]
        j = subarray[1]
        k = subarray[2]
        
        if j == r*i and k == r*j : 
            return 1 ## good triplet
        else:
            return 0 ## bad triplet
            
    else:
        
        for j in range(i+1,len(arr)) : 
    
            subarray.append(arr[j])
            c = c  + subset1(arr,r,j,subarray)
            subarray.pop()
            
    return c 
            
            

def subset(arr,r) :
    
    c = 0 
    for i in range(len(arr)) : 
        c = c  + subset1(arr,r,i,[arr[i]])

    return c 
    
    
print(subset([1 ,5 ,5 ,25 ,125],5))
