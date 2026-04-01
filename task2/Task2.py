import sys

def read_ellipse(file1):
    with open(file1) as f1:
        x0, y0 = map(float, f1.readline().split())
        a, b = map(float, f1.readline().split())
    return x0, y0, a, b


def read_points(file2):
    points = []
    with open(file2) as f2:
        for line in f2:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def check_points(x, y, x0, y0, a, b):
    result = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)

    if result == 1:
        return 0  # точка на окружности
    elif result < 1:
        return 1  # точка внутри
    else:
        return 2  # точка снаружи

file1 = sys.argv[1]
file2 = sys.argv[2]

x0, y0, a, b = read_ellipse(file1)
points = read_points(file2)

for x, y in points:
    print(check_points(x, y, x0, y0, a, b))
