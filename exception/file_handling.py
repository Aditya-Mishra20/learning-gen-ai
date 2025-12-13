# file = open("order.txt", "w")
# try:
#     file.write("Order details: 2 cups of masala chai\n")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("ginger tea - 5 cups\n")