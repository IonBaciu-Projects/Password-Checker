import re

def password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")
        
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[@$!%*?&]", password):
        strength += 2
    else:
        feedback.append("Add at least one special character (@, $, !, %, *, ?, &).")

    if strength >= 7:
        verdict = "Strong"
    elif 4 <= strength < 7:
        verdict = "Medium"
    else:
        verdict = "Weak"

    return verdict, feedback


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result, tips = password_strength(pwd)

    print(f"\nPassword Strength: {result}")
    if tips:
        print("Suggestions to improve your password:")
        for tip in tips:
            print(f"- {tip}")
