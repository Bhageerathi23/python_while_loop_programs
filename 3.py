#1
i = 1
while i <= 50:
    if i % 5 == 0:
        print(i)
    i += 1

#2
i = 5
while i <= 50:
    print(i)
    i += 5

#3
i = 1
while True:
    if i > 50:
        break
    if i % 5 == 0:
        print(i)
    i += 1