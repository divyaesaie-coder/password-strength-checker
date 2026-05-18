#Develop a Python program to check password strength using length, uppercase, lowercase, numbers, and special characters.
p = input("Enter password: ")

score = 0

if len(p) >= 8:
    score += 1
if any(ch.isupper() for ch in p):
    score += 1
if any(ch.islower() for ch in p):
    score += 1
if any(ch.isdigit() for ch in p):
    score += 1
if any(ch in "@#$&_()+/" for ch in p):
    score += 1

if score <= 2:
    print("Password strength: WEAK")
elif score <= 4:
    print("Password strength: MEDIUM")
else:
    print("Password strength: STRONG")  

