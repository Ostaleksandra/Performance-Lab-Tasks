n1 = int(input("Введите число n1: "))
m1 = int(input("Введите число m1: "))

n2 = int(input("Введите число n2: "))
m2 = int(input("Введите число m2: "))

round_arrow1 = list(range(1, n1+1))
round_arrow2 = list(range(1, n2+1))

def interval(round_arrow, m):
    interval_arrow = []
    i = 0
    while True:
        arr = []
        for num in range(m):
            arr.append(round_arrow[(i + num) % len(round_arrow)])
        interval_arrow.append(arr)
        i = (i + m - 1) % len(round_arrow)
        if i == 0:
            return interval_arrow

def first_num(interval):
    arr = []
    for i in interval:
        arr.append(i[0])
    return arr

part1 = first_num(interval(round_arrow1, m1))
part2 = first_num(interval(round_arrow2, m2))

result = part1 + part2

print(''.join(map(str, result)))
