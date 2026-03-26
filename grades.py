Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> p, c, b, m, cs = (map(int, input().split()))
... percentage = (p + c + b + m + cs) / 5
... if percentage >= 90:
...     print("Grade A")
... elif percentage >= 80:
...     print("Grade B")
... elif percentage >= 70:
...     print("Grade C")
... elif percentage >= 60:
...     print("Grade D")
... elif percentage >= 40:
...     print("Grade E")
... else:
