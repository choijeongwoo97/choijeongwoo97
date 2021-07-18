#bool 자료형

x = True

print("type of x : ",type(x))
print("x : ", x)

print(True and False) #둘다 True면 True
print(True or False) #둘 중 하나만 True여도 True

a = 2

print("a < 1 : ", a < 1) #2 < 1이기 때문에 False

c = a > 1 #a > 1의 return값을 c에 저장
print("c = ", c)

print("a > 1 or a < 0 : ", a > 1 or a < 0)