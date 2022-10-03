#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C)
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

ccache = {1: 1}


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


"""def cycle_length (n) :   # Alternative iterative approach
    assert n > 0
    og = n
    c = 1
    while n > 1 :
        if n in ccache:
            ccache[og] = ccache[n] + c - 1
            return ccache[og]
        c += 1
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
    assert c > 0
    ccache[og] = c
    return c"""


def cycle_length(n):
    assert n > 0
    c = -1
    if n == 1:
        return 1
    elif n % 2 == 0:
        c = n//2
    else:
        c = 3*n+1
    if c not in ccache:
        ccache[c] = cycle_length(c)
    return ccache[c]+1


'''if n in ccache: return ccache[n]
    elif n%2==0: return cycle_len(n//2)+1
    else: return cycle_len((3*n)+1)+1'''


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    assert type(i) == int
    assert type(j) == int
    assert i > 0 and j > 0

    max = 0
    if i > j:
        i, j = j, i
    temp = 0

    for x in range(i, j + 1):
        if x % 2 == 0 and x/2 in ccache:
            temp = ccache[x/2]+1
        else:
            temp = cycle_length(x)
            ccache[x] = temp
        # print("Cycle length for ", x, "is:", temp)
        if temp > max:
            max = temp

    return max

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
