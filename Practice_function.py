#function

def f(x): #함수 선언
    result = x + 2
    return result #아웃풋

result = f(x = 10) #함수 호출 / 인자 이름도 함께 작성(key word argment)해주면 코드 이해가 편함 & 인자의 순서 상관 X(optional)

print(result)

#default argument

def func(x, y, const = 0.1):
    return (x + y) * const

print(func(10, 20, 1))
print(func(y=10, x=30))

#cascading (ex func1(func2))

def get_my_lucky_nymber():
    return 7

def my_sum(x,y):
    return x + y

print(my_sum(get_my_lucky_nymber(),5))