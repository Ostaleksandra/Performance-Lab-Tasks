import sys

file = sys.argv[1]

nums = []
with open(file) as f:
    for line in f:
        nums.append(int(line.strip()))

nums.sort()
avg = nums[len(nums) // 2]

steps = 0
for num in nums:
    steps += abs(num - avg)

if steps > 20:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
else:
    print(steps)