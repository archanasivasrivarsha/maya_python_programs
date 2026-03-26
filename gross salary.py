Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> basic = int(input())
... if basic <= 10000:
...     da = basic * 0.80
...     hra = basic * 0.20
... elif basic <= 20000:
...     da = basic * 0.90
...     hra = basic * 0.25
... else:
...     da = basic * 0.95
...     hra = basic * 0.30
... gross = basic + da + hra
