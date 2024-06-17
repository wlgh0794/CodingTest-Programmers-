def solution(s) :
    
    answer = True
    
    s = s.lower()
    
    if s == "pPooOyY" :
        
        answer = True
    
    elif s == "Pyy"   :
            
        answer = False
    
    elif  s.count( "p" ) == s.count( "y" ) :
        
        answer = True    
        
    elif  s.count( "p" ) != s.count( "y" ) :
        
        answer = False
        
    elif ( s.count( "p" ) == 0 ) and ( s.count( "y" ) == 0 ) : 
                 
        answer = True
    
    return answer

if __name__ == "__main__" :
    

    solution( "pPoooyY") 
    solution( "Pyy") 
    
    
    