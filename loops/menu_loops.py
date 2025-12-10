seasons = ["Spring", "Summer", "Fall", "Winter"]
months = ["March", "June", "September", "December"]

# for idx, s in enumerate(seasons, start=1):
#     print(f"the {idx} season is: {s}")

for i in range(0,3):
    print(f" the {i} season is: {seasons[i]}")
    

#using zip

for s, m in zip(seasons, months):   
    print(f"{m} is in {s}")