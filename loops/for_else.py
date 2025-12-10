staff = [("Alice", 16), ("Bob", 12), ("Charlie", 15)]

for name, age in staff: 
    if age > 18:
        print(f"{name} is over 18. ")
        break
else: print("No staff member is over 18.")