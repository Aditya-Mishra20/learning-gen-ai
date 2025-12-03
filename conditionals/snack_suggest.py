# snack = input("What snack would you like? ").lower()

# if snack == "chips":
#     print("You selected chips.")
# elif snack == "chocolate":
#     print("You selected chocolate.")
# else:
#     print("Snack not recognized.")



size = input("Choose a size (small, medium, large): ").lower()
total_price = 0
if size == "small":
    print("You selected a small snack for 10 Rs.")
    total_price += 10
elif size == "medium":
    print("You selected a medium snack for 20 Rs.")
    total_price += 20
elif size == "large":
    print("You selected a large snack for 30 Rs.")
    total_price += 30
else:
    print("Invalid size selected.")

print(f"Total price: {total_price} Rs.")