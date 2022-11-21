# For Loop - Range Function
# for number in range (a, b):
    # print(number)
numbers = []

for number in range(1, 11):
    numbers.append(number)

print(numbers)

print("\n##########\n")

for number in range(1, 11, 3):
    print(number)

print("\n##########\n")

sum = 0

for number in range(1, 101):
    sum += number

print(sum)
