# Addition of numbers with Recursion

def add(a):
  # print(a)
  if(a==0):
    return 0
  else:
    total  = a + add(a-1)
    return total


sum = add(5)
print(sum)
