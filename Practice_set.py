#set 자료형 => 데이터의 중복 저장을 막기위해 사용

a_set = {1, 2, 3, 1} #중복 데이터는 하나만 저장
a_list = [1, 2, 3, 1] #중복 데이터는 하나만 저장

print("a_set : ", a_set)
print("a_list : ",a_list) #중복 데이터도 전부 저장

new_a_list = set(a_list) #list => set으로 변환
print("new_a_list : ", new_a_list) #중복 데이터는 하나만 저장