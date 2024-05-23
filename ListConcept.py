score = [10, 20, 30, 40, 50]
print(score)

print(score[0])
print(score[4])
print(score[-1])
print(score[-5])

# New Copy or shallow of lists
print(score[:])

print(score + [1, 2, 3])
print(score + ["A", "B", "C"])

score2 = [10, 11, 12, 13, 14, 15]
score2[3] = 23
print(score2)

# Append
score2.append(16)
print(score2)
score2.append(7 ** 3)
print(score2)

name = ['a', 'b', 'c', 'd', 'e']
print(name)
name[2:5] = ['F', 'G', 'H']
print(name)
name[2:5] = []
print(name)

# Nested Lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[1])
print(x[0][1])
print(x[1][1])
