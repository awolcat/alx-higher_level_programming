#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = []
    ans = []
    if len(tuple_a) == 2 and len(tuple_b) == 2:
            tuple_1 = list(tuple_a) + list(tuple_b)
        else:
            tuple_1.append(tuple_a[i])
    for i in range(1):
        if tuple_b[i] == None:
            tuple_1.append(0)
        else:
            tuple_1.append(i)
    print(tuple_1)

    ans = tuple_1[0] + tuple_1[2], tuple_1[1] + tuple_1[3]
    tuple(ans)
    return ans
