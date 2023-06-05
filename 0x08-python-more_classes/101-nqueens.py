#!/usr/bin/python3
"""
    This module contains algorithms for solving
    the nqueen problem
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)
