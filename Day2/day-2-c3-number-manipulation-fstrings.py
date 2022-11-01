## Number Manipulation
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))
print(8 // 3) # Floor division, no need to convert into an integer

print ("\n##########\n")

print(type(4 / 2))
print(type(4 // 2))

print ("\n##########\n")

score = 9
score -= 1
score /= 2
score += 3

print(score)

print ("\n##########\n")

## F Strings
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, your are winning is {isWinning}")
