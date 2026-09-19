import re


def audit_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters. 12 or more is recommended.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Check common weak passwords
    common_passwords = [
        "password",
        "12345678",
        "123456789",
        "password123",
        "qwerty123",
        "admin123",
        "welcome123"
    ]

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common or easily guessed passwords.")

    # Determine security level
    if score >= 6:
        strength = "STRONG"
    elif score >= 4:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    print("\n" + "=" * 55)
    print("           WI-FI PASSWORD SECURITY AUDITOR")
    print("=" * 55)

    print("\nPassword Security Result")
    print("-" * 55)
    print("Password Length:", len(password))
    print("Security Score:", score, "/ 6")
    print("Security Level:", strength)

    print("\nSecurity Suggestions")
    print("-" * 55)

    if suggestions:
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Password meets the recommended security requirements.")

    print("\n" + "=" * 55)
    print("Security audit completed.")
    print("=" * 55)


print("=" * 55)
print("           WI-FI PASSWORD SECURITY AUDITOR")
print("=" * 55)

password = input("Enter Wi-Fi password to audit: ")

if password:
    audit_password(password)
else:
    print("Error: Password cannot be empty.")
