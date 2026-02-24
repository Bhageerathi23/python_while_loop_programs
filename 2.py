#1
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1


#2
i = 1
while i <= 20:
    print(i)
    i += 2


#3
i = 1
while True:
    if i > 20:
        break
    if i % 2 != 0:
        print(i)
    i += 1


#4
i = 1
while i <= 20:
    print(i, end=" ")
    i += 2