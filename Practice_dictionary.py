#dictionary 자료형 (hash table)

my_dict = {123: 456,
        "my_key": "my_value"} #key:value
print("my_dict : ", my_dict)
print("my_dict[my_key] : ", my_dict["my_key"])

my_dict = dict(my_value = 456, my_key = 1000) #함수 호출 형태로 dictionary 만들기 이 때 숫자는 Key가 될 수 없음
print("my_dict : ", my_dict)

stock_dict = {
    "삼성전자" : 100,
    "현대 자동차" : 90
}

print("stock_dict : ", stock_dict)
print("stock_dict[삼성전자] : ", stock_dict["삼성전자"])
stock_dict["삼성전자"] = 120 #삼성전자 변경
print("stock_dict : ", stock_dict)
stock_dict["하이닉스"] = 100 #하이닉스 추가
print("stock_dict : ", stock_dict)