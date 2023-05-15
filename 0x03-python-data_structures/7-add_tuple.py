#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = []
    tuple_2 = []
    ans = []
    tuple_1 = list(tuple_a + tuple_b)
    print(tuple_1)
    for i in range(4):
        if tuple_1[i] == None:
            tuple_2[i] = 0
        tuple_2[i] += tuple_1[i]

    ans = tuple_2[0] + tuple_2[2], tuple_2[1] + tuple_2[3]
    tuple(ans)
    return ans
