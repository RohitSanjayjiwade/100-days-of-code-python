List = [2,3,5,6,7,8,9,1,3,7,5,6,44,66,33]
print(List)

# List.sort()               # Sorts the list in ascending order
# print(List)

# List.sort(reverse=True)   # reverse=True is used to reverse the list
# print(List)

# -----------------------------------------------------------------
# Add the elements of the list
List.append(100)            # Adds 100 to the end of the list

# -----------------------------------------------------------------
# Remove the last element from the list
# List.pop()                  #removes last element

# Remove the element at index 0
# List.pop(0)                 #removes first element (Index)

# --------------------------------------------------------------------
# Remove First Occurrence of Element
# List.remove(33)              #removes first occurence of 33

# ------------------------------------------------------------------
# Insert the element at the given index
List.insert(0,100)           #inserts 100 at index 0
print(List)

# --------------------------------------------------------------
# Reverse a list
# List.reverse()               #reverses the list

# ------------------------------------------------------------------------
# Get The Index of an item
print(List.index(6))        #returns index of first occurence of 6

# ------------------------------------------------------------------------
# Count the Item
print(List.count(100))      #returns count of 100

List2 = [101,102,103,104,105]
# --------------------------------------------------------------------

# Copy List

# m = List2               # m is a reference to List2
# m[0] = 0                # changes the value of List2    
# print(List2) 
# print(m)


# m = List2.copy()         # m is a copy of List2
# m[0] = 0
# print(List2)
# print(m)
# --------------------------------------------------------------------
# Extend
# List.extend(List2)         #adds List2 to the end of List
# print(List)

# -------------------------------------------------------------------
# Concatenat List
k = List + List2          #concatenates List and List2
print(k)

# --------------------------------------------------------------------
# Clear the list
List.clear()
print(List)

