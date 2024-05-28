def solution(n, k):
    
    answer = []
    
    Data_list = []

    for i in range( 1 , n + 1) :
        
        Data_list.append( i )
        
    for j in Data_list :
        
        if ( j % k == 0 ) :
        
            answer.append( j )

    return answer


if __name__ == "__main__" :
    
    n_list = [ 10 , 15 ]
    k_list = [ 3 , 5 ]
    
    for i in range( 0 , 2 ) :
    
        print( "결과 : " , solution( n_list[i] , k_list[i] ) )
        
    
    
    
    
    
    
    
    