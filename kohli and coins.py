Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> X = int(input())
... if X % 5 != 0:
...     print(-1)
... else:
...     tens = X //10
...     remaining = X % 10
...     fives = remaining // 5
