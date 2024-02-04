"""Function:
1 -> Without parameter Without returntype
2 -> Without parameter With returntype
3 -> With parameter Without returntype
4 -> With parameter With returntype """

# ----------------------------------------
def add():
  a = 10
  b = 20
  c = a+b
  print("Without parameter Without returntype : ",c)

add()

# ----------------------------------------
def add1():
  a = 10
  b = 20
  c = a+b
  return c

addd = add1()
print("Without parameter With returntype : ",addd)

# ------------------------------------------
def add2(a,b):
  c = a+b
  print("With parameter Without returntype : ",c)

add2(10,20)

# -------------------------------------
def add3(a,b):
  c = a+b
  return c

result = add3(10,20)
print("With parameter With returntype : ",result)

# -----------------------------------------

# pass

def add4():
  pass

