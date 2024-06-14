def solution(num1, num2):
    
    answer = num1 % num2
    
    return answer

if __name__ == "__main__" :
     
    Data_list1 = [ 3  , 10 ]
    
    Data_list2 = [ 2 , 5 ]
    
    for i in range(2) :
          
        print( solution( Data_list1[i] , Data_list2[i] ))