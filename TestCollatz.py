#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C)
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.6/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, ccache

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "4 6\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  4)
        self.assertEqual(j, 6)

    def test_read_3(self):
        s = "100001 500000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100001)
        self.assertEqual(j, 500000)

    def test_read_4(self):
        s = "1000 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1000)
        self.assertEqual(j, 100)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6(self):
        v = collatz_eval(999999, 999999)
        self.assertEqual(v, 259)

    def test_eval_7(self):
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)

    def test_eval_8(self):
        v = collatz_eval(999990, 999999)
        self.assertEqual(v, 259)

    def test_eval_9(self):
        v = collatz_eval(1000, 5000)
        self.assertEqual(v, 238)

    def test_eval_10(self):
        v = collatz_eval(5001, 10000)
        self.assertEqual(v, 262)

    def test_eval_11(self):
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    def test_eval_12(self):
        v = collatz_eval(10001, 50000)
        self.assertEqual(v, 324)

    def test_eval_13(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_14(self):
        v = collatz_eval(50001, 100000)
        self.assertEqual(v, 351)

    def test_eval_15(self):
        v = collatz_eval(100, 1000)
        self.assertEqual(v, 179)

    def test_eval_16(self):
        v = collatz_eval(100001, 500000)
        self.assertEqual(v, 449)

    def test_eval_17(self):
        v = collatz_eval(500001, 999999)
        self.assertEqual(v, 525)

    def test_eval_18(self):
        v = collatz_eval(4, 6)
        self.assertEqual(v, 9)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 1000, 179)
        self.assertEqual(w.getvalue(), "100 1000 179\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1000, 5000, 238)
        self.assertEqual(w.getvalue(), "1000 5000 238\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 5001, 10000, 262)
        self.assertEqual(w.getvalue(), "5001 10000 262\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("17 38\n5001 10000\n100 1000\n1 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "17 38 112\n5001 10000 262\n100 1000 179\n1 999999 525\n")

    def test_solve_3(self):
        r = StringIO("69 420\n41 301\n7680 8500\n2020 5050\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "69 420 144\n41 301 128\n7680 8500 252\n2020 5050 238\n")

    def test_solve_4(self):
        r = StringIO("84115 82967\n10 100\n89 94\n338 883\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "84115 82967 289\n10 100 119\n89 94 106\n338 883 179\n")

# ----
# main
# ----


if __name__ == "__main__":
    main()

""" #pragma: no cover
$ coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


$ coverage report -m                   >> TestCollatz.out



$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
