i = 0
while i<7:
  print(i)
  i = i + 1
  if i == 4:
    break

else:
  print("Sorry no i",i)
print("i",i)



for x in range(5):
  # print ("iteration no {} in for loop".format(x+1))
  print (f"iteration no {x+1} in for loop")
  if((x+1)==3):
    break
else:
  print ("else block in loop")
print ("Out of loop")




for x in range(5):
  # print ("iteration no {} in for loop".format(x+1))
  print (f"iteration no {x+1} in for loop")
else:
  print ("else block in loop")
print ("Out of loop")
