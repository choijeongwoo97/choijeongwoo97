#while문

i = 0
while i < 10:
    print(i)
    i += 1

i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

a = 1
while a<=5 or a>2:
    a = a + 1
    if a == 3:
        continue
    if a==10:
        break

    print(a)