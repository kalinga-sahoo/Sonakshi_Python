#Reverse the name in python
Name=input("Enter the name:")
name_tup=tuple(Name.split())
reverse_tuple=name_tup[::-1]
print(" ".join(reverse_tuple))