#tuples 
'''
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))
my_tuple2 = ("apple", "banana", "cherry")
print(my_tuple2)

(fruit1, fruit2, fruit3) = my_tuple2

print(f"1st:{fruit1}, 2nd: {fruit2}")
print(my_tuple2[2])


hello, world = 1, 2
print(f"Before Swap: hello={hello}, world={world}")
hello, world = world, hello
print(f"After Swap: hello={hello}, world={world}")
'''
# Exercises on Tuples   
'''
Q1 Problem:
Given a tuple:
'''
#t = (10, 20, 30, 40, 50, 60)
'''
Extract the first three elements.
Extract every second element starting from the second element.
Hint: Use indexing and slicing.
'''
'''
first_three = t[0:3]
print(f"First three elements: {first_three}")
print(f"every second element starting from the second element: {t[1::2]}")
'''

'''
2. Tuple Immutability

Problem:
You have a tuple:
'''
#t = (1, 2, 3, 4)
'''
Try changing the second element to 10.
Catch the error and create a new tuple with the change instead.
Hint: Tuples are immutable; you’ll need to convert to a list or use concatenation.
'''
'''
new_t = (t[0], 10, t[2], t[3])
print(f"Original tuple: {t}")
print(f"New tuple with change: {new_t}")
#OR
lst = list(t)
lst[1] = 10
new_t2 = tuple(lst)
print(f"New tuple with change using list conversion: {new_t2}")
'''

'''
3. Tuple Unpacking
Problem:
You have a tuple representing a point in 3D space:
'''
#point = (4, 5, 6)
'''
Unpack the tuple into variables x, y, z.
Print them in the format: "x=4, y=5, z=6".
Hint:Use tuple unpacking.
'''
'''
x, y, z = point
print(f"x={x}, y={y}, z={z}")
'''

''' 
4. Nested Tuples

Problem:
You have a nested tuple of students with (name, marks):
'''
# students = (("Alice", 85), ("Bob", 90), ("Charlie", 18))
'''

Print the names of students who scored more than 80.

Hint: Loop through the tuple and access nested elements.
'''

# for stud in students:
#     name,marks = stud
#     if marks > 80:
#         print(name)


'''
5. Count and Index Methods

Problem:
Given the tuple:
'''
t = (1, 2, 3, 2, 2, 4, 5)

'''
Find how many times 2 occurs.

Find the index of the first occurrence of 4.

Hint: Use the tuple methods .count() and .index().
'''

# count_2 = t.count(2)
# index_4 = t.index(4)

# print(f"2 occurs {count_2} times.")
# print(f"The index of the first occurrence of 4 is {index_4}.")  


#membership testing
print(f"Is 3 in tuple? { 3 in t}")


















