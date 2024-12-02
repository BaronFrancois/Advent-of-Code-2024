with open("day_1_input.txt", "r") as file:
    lines = file.readlines()

# Extraire les deux colonnes
left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)


left_list.sort()
right_list.sort()


paired_list = []


for i in range(len(left_list)):
    paired_list.append((left_list[i], right_list[i]))


# print(paired_list)


total_distance = 0
for a, b in paired_list:
    total_distance += abs(a - b)


print(total_distance)
