
def solution(n):
    
    answer = 0
    
    Datas = []
    
    for i in range( 1 , n + 1 ) :
    
        if n % i == 0 :
            
            Datas.append( i )
    
    for Data in Datas :
        
        answer += int( Data )
        
    return answer


if __name__ == "__main__" :
    
    print( solution( 12 ) ) 
        
    print( solution( 5 ) ) 