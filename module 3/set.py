my_set = {1,2,3}

my_set = set([1,2,3,4,5])

my_set = set()

my_set = {1,2,2,3,3,3}

print(my_set)

set1 = {1,2,3}
set2 = {3,4,5}

union_result_method = set1.union(set2)
union_result_operator = set1 | set2

print("Union of set1 and set2:", union_result_method)
print("Union of set1 and set2:", union_result_operator)

intersection_result_method = set1.intersection(set2)
intersection_result_operator = set1 & set2

print("intersection of set1 and set2:", intersection_result_method)
print("intersection of set1 and set2:", intersection_result_operator)

difference_result_method = set1.difference(set2)
difference_result_operator = set1 - set2

print("difference of set1 and set2:", difference_result_method)
print("difference of set1 and set2:", difference_result_operator)

symmetric_difference_result_method = set1.symmetric_difference(set2)
symmetric_difference_result_operator = set1 ^ set2

print("symmetric_difference of set1 and set2:", symmetric_difference_result_method)
print("symmetric_difference of set1 and set2:", symmetric_difference_result_operator)

my_set = {1,2,3}

my_set.add(7)

my_set.remove(3)

my_set.discard(8)

print(my_set)

my_set.clear()

print(my_set)