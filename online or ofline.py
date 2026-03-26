Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> N, M = map(int, input().split())
... online_price = N * 0.9
... if online_price < M:
...     print("ONLINE")
... elif online_price > M:
...     print("DINING")
... else:
