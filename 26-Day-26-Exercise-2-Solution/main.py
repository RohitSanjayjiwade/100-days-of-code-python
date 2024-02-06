import time

t = time.strftime("%H:%M:%S")
print(t)

h = int(time.strftime("%H"))

# h = int(input("Enter the time: "))

if (h >= 0 and h < 12):
  print("Good Morning Sir")
elif (h >= 12 and h < 17):
  print("Good Afternoon Sir")
elif (h >= 17 and h < 20):
  print("Good Evening Sir")
else:
  print("Good Night Sir")
