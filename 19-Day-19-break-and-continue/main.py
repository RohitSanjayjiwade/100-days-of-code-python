# num = int(input("Enter a number: "))
# for i in range(1,11):
#   print(num, "X" ,i, "=", num*i)
#   if i == 5:
#     break


# num = int(input("Enter a number: "))
# for i in range(1,11):
#   if i == 5:
#     continue
#   print(num, "X" ,i, "=", num*i)


# for i in range(10):
#   print(i+1)
#   if(i==4):
#     break


# for i in range(10):
#   if(i%2==0):
#     continue
#   print(i)

# for i in range(50):
#   print((i+1)*2)



# do while Loop

while(True):
  num = int(input("Enter a number: "))
  print(num)
  if not num > 0:
    break

while True:
    # code to be executed
    user_input = input("Do you want to continue? (yes/no): ")

    if user_input.lower() != 'yes':
        break  # exit the loop if the user enters anything other than 'yes'

print("End of loop.")