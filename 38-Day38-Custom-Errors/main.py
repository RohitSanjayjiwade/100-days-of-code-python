a = input("Enter any value between 5 and 9 : ")
try:
  if (a.lower() == "quit"):
    print(a)
    print("You have quit the program")
  elif (int(a) < 5 or int(a) > 9):
    raise ValueError("\nValue should be between 5 and 9")
  else:
    print("\nYou have entered the correct value")

except ValueError as e:
  print(e)
except Exception:
  print("\nNameError")



# if(5<=int(a)<=9):
