a = 10
b = 20

# print(a) if(a>b) else print(b)                  # 20
# print(a) if(a>b) else print(b) if(b>a) else print("hi")   # hi

c = 30

print(a) if (a > b and a > c) else print(b) if (b > c) else print(c)

c = 9 if (a > b) else 0
print(c)
