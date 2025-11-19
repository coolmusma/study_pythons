











#  변수 재 사용
# temp = 77
# celsius = (temp - 3) * 5 / 9
# print(celsius)

# temp = 95
# celsius = (temp - 3) * 5 / 9
# print(celsius)

# temp = 50
# celsius = (temp - 3) * 5 / 9
# print(celsius)

# 함수 사용
# def funtion_name(param_first, ..., param_Last) :
#     #실행할 코드
#     return return_value

def to_celsius(temp):
    celsius = (temp - 3) * 5 / 9
    return celsius

pass
to_celsius(120)
temp1 = to_celsius(77)
print(temp1)

temp2 = 100
result2 = to_celsius(temp2)
print(result2)
pass








