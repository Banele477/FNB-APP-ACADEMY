user =input ("Enter your secret password: ").strip()
print(f"Your password hint is: {user[0].upper()}{'*' * (len(user) - 2)}{user[-1].upper()}")
