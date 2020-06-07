import re 

class Solution:
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        LETTER_LOG=[]
        DIGIT_LOG=[]
        
        for log in logs : 
            
            if log.split(" ")[1][0] in [str(i) for i in range(10)] : 
               
                DIGIT_LOG.append(log)
            
            else:
                identifier = log.split(" ")[0]
                rest = " ".join(log.split(" ")[1: ])
                LETTER_LOG.append((identifier,rest))
                
      
        
        sorted_TIE_ID = sorted(LETTER_LOG,key=lambda x:x[0])
        sorted_LETTER_LOG = sorted(sorted_TIE_ID,key=lambda x:x[1])
      
    
        return [x[0]+" "+x[1] for x in sorted_LETTER_LOG] + DIGIT_LOG
       
                
        
        
       
        
        
            
        
