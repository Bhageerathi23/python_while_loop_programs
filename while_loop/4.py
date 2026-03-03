#
i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)

#
i = 1
total = 0

while True:
    if i > 10:
        break
    total += i
    i += 1

print("Sum =", total)