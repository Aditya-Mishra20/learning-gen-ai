#set

mySet = {1, 2, 3, 4, 5}
mySet2 = {4, 5, 6, 7, 8}

res = mySet.intersection(mySet2) 
#OR
# res = mySet & mySet2
print(f'Intersection of sets: {res}')
res2 = mySet.union(mySet2)
#OR
res3 = mySet | mySet2
print(f'Union of sets: {res2}')
print(f'Union of sets: {res3}')