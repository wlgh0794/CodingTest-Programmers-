def solution(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__" :
    
    
    numbers_list = [
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ,
                    [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]      
    ]


    for i in numbers_list :
        
        solution( i )

