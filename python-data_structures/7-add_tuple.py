#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    sum_t = []
    if a_len >= 2 and b_len >= 2:
        sum_t.append(tuple_a[0] + tuple_b[0])
        sum_t.append(tuple_a[1] + tuple_b[1])
        x = tuple(sum_t)
        return x
    if a_len < 2 and b_len < 2:
        sum_t.append(tuple_a[0] + tuple_b[0])
        sum_t.append( 0 + 0);
        x = tuple(sum_t)
        return x
