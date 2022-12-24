input_data = input()
row = int(input_data[1])
columns = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_columns = columns + step[1]
    if next_row >= 1 and next_row <= 8 and next_columns >= 1 and next_columns <= 8:
        result += 1
print(result)