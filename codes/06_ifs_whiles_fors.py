second = "Programming"
first = f"Welcome to Python Strings {second}"

print(first)



first = 5

while first > 0:
    print(first)
    first = first - 1

kor = [70, 80, 90, 40, 50]                                                                                                             
eng = [90, 80, 70, 70, 60]                                                                                                                                                                                                                                                  
                          
sum_all = sum(kor) + sum(eng)                                                                                                          
                                                                                              
print(f"전체 합계: {sum_all}")                                                                                                         
                
                

1 kor = [70, 80, 90, 40, 50]  # kor 리스트 정의 추가                                                                                     
2 eng = [90, 80, 70, 70, 60]  # eng 리스트 정의 추가                                                                                     
3                                                                                                                                        
4 sum_total = 0                                                                                                                          
5                                                                                                                                        
6 for i in range(len(kor)):  # range(5)와 같음. i는 0~4까지 변함                                                                         
7     sum_total = sum_total + kor[i] + eng[i]  # for 루프 안에 들여쓰기                                                                  
8                                                                                                                                        
9 print(f"{sum_total}")  # print 문법 수정   
