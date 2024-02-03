num = int(input("Enter Number to perform operations : "))
n = 0

while n!=5:
  print("Choose the Option 1. Square 2. Factorial 3. Prime 4. Odd/Even 5. Exit")
  n = int(input("Enter your choice : "))
  match n:
    case 1:
      print("Square of ",num," is ",num*num)
    case 2:
      fact = 1
      for i in range(1, num+1):
        fact = fact*i
      print("Factorial of ",num," is ",fact)
    case 3:
      for i in range(2, num):
        if (num%i == 0):
          print(num," is not a Prime Number")
          break
      else:
        print(num," is a Prime Number")
    case 4:
      if(num%2 == 0):
        print(num," is an Even Number")
      else:
        print(num," is an Odd Number")
    case 5:
      print("Exiting...")
    case _:
      print("Invalid Choice")
      
        


# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")

#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)
