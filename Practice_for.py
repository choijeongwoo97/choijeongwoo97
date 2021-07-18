#for문

for i in range(10, 50, 10):
    print(i)

for i in range(50, 90):
    if i % 2 ==0:
        print(i, "는 짝수입니다.")

for i in range(10):
    if i == 5:
        break #조건이 맞으면 중단
    print(i)

for i in range(10):
    if i < 5:
        continue #조건이 맞으면 다시 for문으로
    print(i)