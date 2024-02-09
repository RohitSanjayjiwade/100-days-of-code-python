try:
  n = int(input("Enter the Number: "))
  print(f"Multiplication Table of {n} is:")
  for i in range(1,11):
    print(f"{n} X {i} = ",n*i)
except ValueError:
  print("Invalid Input")
except IndexError:
  print("Index Error")
except Exception as e:
  print(e)
  print("Some Error Occured")

# -----------------------------------------------------------

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")

except IndexError:
  print("Index Error")
except Exception:
  print("Some Error Occured")
