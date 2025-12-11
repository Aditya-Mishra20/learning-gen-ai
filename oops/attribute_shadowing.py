class Chai:
    temperature = "Hot"
    



cutting_tea = Chai()

cutting_tea.temperature = "Warm"
cutting_tea.flavor = "Ginger"

print(cutting_tea.temperature)
print(cutting_tea.flavor)

del cutting_tea.temperature
del cutting_tea.flavor
print(cutting_tea.temperature)
print(cutting_tea.flavor)