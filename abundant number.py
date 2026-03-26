Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> n = int(input())
... sum_factors = 0
... for i in range(1, n):
...     if n % i == 0:
...         sum_factors += i
... if sum_factors > n:
...     print(True)
... else:
