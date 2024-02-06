letter = "Hey my name is {0} and I am from {1}"
country = "India"
name = "Rohit"

print(letter.format(name,country))
print(letter)

print(f"Hey my name is {{name}} and I am from {country}")


txt = "For only {price:.2f} dollars!"

print(txt.format(price = 49.09999))
print(txt)

price = 49.09999
print(f"For only {price:.2f} dollars!")


print(2*30)
print(f"{2*30}")