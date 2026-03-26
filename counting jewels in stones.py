Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> jewels = input().strip()
... stones = input().strip()
... jewel_set = set(jewels)
... count = 0
... for ch in stones:
...     if ch in jewel_set:
...         count += 1
