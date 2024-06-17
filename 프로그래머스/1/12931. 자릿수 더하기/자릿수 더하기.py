def solution(n):
    
    answer = 0
      
    input_Data = str( n )
    
    
    for Data in input_Data :
         
        answer += int(Data)
                                                 
    return answer


if __name__ == "__main__" :
    
    print( solution( 123 ) )
    print( solution( 987 ) )