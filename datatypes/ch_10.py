my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"])
del my_dict["age"]
my_dict["city"] = "Los Angeles"
print(my_dict)

res = my_dict.get("age", "Not Found")
res2 = my_dict.get("name", "Not Found")
print(res)
print(res2)