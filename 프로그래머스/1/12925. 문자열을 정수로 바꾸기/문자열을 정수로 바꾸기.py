def solution(s):
    
    answer = 0
    
    result = 0
    
    if s.count( "-" ) == 0 :

        if int(s) == 0 :

            print("오류")

            return

        elif int(s) > 0 :

            pass
        
    else :
   
        if int(s) < 0 :

            pass       
        
    return int( s )


if __name__ == "__main__" :
    
    pirnt( "결과 : " + solution( "1234" ) )    
    
    
    