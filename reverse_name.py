#Reverse the name in python
Name=input("Enter the name:")
name_tup=tuple(Name.split())
reverse_tuple=name_tup[-1:] + name_tup[:-1]
print(" ".join(reverse_tuple))
match name_tup[-1]:
    case "sahoo":
        print(f"correct surname")
    case _:
        print(f"sername is incorrect")