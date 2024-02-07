#  Factorial of a number using Recursion

def fact(n):
  # print(n)
  if n == 0 or n == 1:
    return 1
  else:
    total =  n * fact(n-1)
    return total


n = int(input("Enter a number: "))
a = fact(n)
print(a)