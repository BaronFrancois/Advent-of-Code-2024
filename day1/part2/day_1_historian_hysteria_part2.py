from collections import Counter
# counter is used to count the occurences within a list

with open("day1\\part2\\day_1_input_part2.txt", "r") as file:
    lines = file.readlines()
# print(lines)

left_list = []
right_list = []

for line in lines:
    #map = converting strings into int
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# counter is used to count the occurences within a list into dictionnary 
# the key is the number and the value the * of time we have the same number
# ex: Counter([3, 3, 2, 1, 3]) -> {3: 3, 2: 1, 1: 1}
right_count = Counter(right_list) 

similarity_score = 0

for num in left_list:
    if num in right_count:
        similarity_score += num * right_count[num]


print("Similarity Score:", similarity_score)
