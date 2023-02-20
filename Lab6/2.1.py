import random

def fill_tuple(max, min):
    list_for_tuple = list()
    for i in range(10):
        list_for_tuple.append(random.randint(min,max))
    return list_for_tuple

tuple1 = tuple(fill_tuple(5, 0))
tuple2 = tuple(fill_tuple(0, -5))

print('tuple1: ', tuple1)
print('tuple2: ', tuple2)

tuple_union = tuple1 + tuple2
print('tuple_union: ', tuple_union)
print('Count of Zero: ', tuple_union.count(0))