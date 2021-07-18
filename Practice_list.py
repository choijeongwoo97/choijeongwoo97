# list

class_score = [90, 30, 60, [12,16]]

print("class_score : ", class_score)

#indexing

print("class_score[3] : ", class_score[3])
print("class_score[-1] : ", class_score[-1]) #-1 인덱싱 처음에서 -1하면 마지막 값
print("class_score[0:2] : ", class_score[0:2]) #범위 인덱싱 : 0<= 출력 <2 0은 생략 가능
print("class_score[1:] : ", class_score[1:]) #범위 인덱싱 : 인덱스 1부터 나머지 전부

#다차원 list

list = [[1, 2],
        [10, 20, 30],
        [100, 200, [300, 400]]]
print("list : ", list)