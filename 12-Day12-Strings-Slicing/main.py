name = "Rohit,Chetan"
print(name[0:5])
print(len(name))

fruit = "Mango"
mangoLen = len(fruit)
print("Mango is a ", mangoLen, "letter word.")

# print(fruit[0:4])
# print(fruit[1:4])
# print(fruit[:])
# print(fruit[:5])
# print(fruit[0:-3])            # 0:5-3 = 0:2      output: Ma
# print(fruit[:len(fruit)-3])   # same as above    output: Ma
# print(fruit[-1:len(fruit)-3])   # 5-1:5-3 = 4:2  output: nothing
print(fruit[-3:-1])  # 5-3:5-1 = 2:4   output: ng

# Quick Quiz:

nm = "Rohit"
print(nm[-4:-2])  # 5-4:5-2 = 1:3  output: oh
