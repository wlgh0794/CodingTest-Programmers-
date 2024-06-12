def solution(num1, num2):
    answer = num1 // num2
    return answer


if __name__ == "__main__" :
    
    Data_list1 = [ 10 , 7 ]
    Data_list2 = [ 5 , 2 ]
    
    
    for i in Data_list1 :
        
        for j in Data_list2 :
            
            solution( i , j )