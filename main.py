import random

answer = "{:03d}".format(random.randint(0, 999))
num_challenges = 0

while True:
    num_challenges += 1

    while True:
        number = input("input 3-digit number: ")
        if number.isdecimal() and len(number) == 3:
            break

    hit = 0
    blow = 0

    for i in range(3):
        digit = number[i]
        for j in range(3):
            if digit == answer[j]:
                if i == j:
                    hit += 1
                else:
                    blow += 1

    if hit == 3:
        break

    print("hit: %d, blow: %d" % (hit, blow))

print("HIT!!! You tried %d times to hit the number." % num_challenges)