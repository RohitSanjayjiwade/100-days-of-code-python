marks = [3, 5, 6, 6, "Rohit", True]
print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[6-3]) # Positive index
# print(marks[3]) # Positive index

# if 6 in marks:
#   print("Yes")
# else:
#   print("No")

# print(marks[:])
# print(marks[0:5])
# print(marks[1:-1])
# print(marks[1:6:2])
# marks.append(10)
# print(marks)
# -------------------------------------------------------

# List Comprehension : 

# lst = [i*i for i in range(10) if i%2==0]
# print(lst)

# lst1 = list(range(10))
# print(lst1)

names = ["Milo", "Sarah", "Rohit", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "h" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 5)]
print(namesWith_O)