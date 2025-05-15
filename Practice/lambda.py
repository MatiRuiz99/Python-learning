from functools import reduce
#Lambda is used when a function would have 1 purpouse only, to not make it be redundant
#code to sort tuples inside a list, first by 2nd value then 3rd if necessary.

values = [(3, "c", "ok"), (1, "a", "hello"), (2, "a", "world") ]

sorted_values = sorted(values, key= lambda x: x[1] + x[2])

print(list(sorted_values))

#using reduce
numbers = [1,2,3,4,5]

#reduce to sum list w/o initializer
result = reduce(lambda acc, x:acc + x, numbers)
print(f"sum of list {result}") #output should be 15

#reduce to find maximum value
max_result = reduce (lambda acc, x: acc if acc > x else x, numbers)
print(f"Max in list {max_result}")