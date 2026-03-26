Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> units = int(input())
... if units <= 199:
...     bill = units * 1.20
... elif units < 400:
...     bill = units * 1.50
... elif units < 600:
...     bill = units * 1.80
... else:
...     bill = units * 2.00
... if bill  > 400:
...     bill = bill + (0.15 * bill)
... else:
...     bill = bill + 100
