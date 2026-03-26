Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a, b, c = map(int, input().split())
... if a >= b and a >= c:
...     print(a)
... elif b >= a and b >= c:
...     print(b)
... else:
