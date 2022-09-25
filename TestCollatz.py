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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

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
        v = collatz_eval(1000, 100)
        self.assertEqual(v, 179)

    def test_eval_17(self):
        v = collatz_eval(100001, 500000)
        self.assertEqual(v, 449)

    def test_eval_18(self):
        v = collatz_eval(500000, 100001)
        self.assertEqual(v, 449)

    def test_eval_19(self):
        v = collatz_eval(500001, 999999)
        self.assertEqual(v, 525)

    def test_eval_20(self):
        v = collatz_eval(69, 69)
        self.assertEqual(v, 15)


    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 1\n100 200 1\n201 210 1\n900 1000 1\n")

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
