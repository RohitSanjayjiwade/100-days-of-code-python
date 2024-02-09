# def func():
#   try:
#     l = [1,2,3,4,5]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occured")
#     return 0
  
#   finally:
#     print("I am always executed")



# x = func()
# print(x)\

i = 0
while(i<3):
  try:
    n = int(input("Enter the Number: "))
    print(n)
    break
  except:
    i = i+1
    print("Please try Again Later")
