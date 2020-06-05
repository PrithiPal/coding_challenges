from collections import Counter

def kth_most_freq(mystr,k) : 
    
    c = Counter(mystr)
    c2 = {}
    
    vals = sorted( list(set(c.values())), reverse=True)
    
    kth_freq = vals[k-1]
    
    
    for k in c : 
        if c[k]==kth_freq:
            return k 

    
print(kth_most_freq("GeeksForGeeks",3))
