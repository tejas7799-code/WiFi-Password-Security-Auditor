# Wi-Fi Password Security Auditor

## Project Overview

Wi-Fi Password Security Auditor is a basic cybersecurity project developed using Python.

The application evaluates the security of a Wi-Fi password based on common password security requirements such as password length, uppercase letters, lowercase letters, numbers, and special characters.

The tool provides a security score, classifies the password as Weak, Medium, or Strong, and provides suggestions for improving password security.

> This project only audits a password entered by the user. It does not access, retrieve, crack, or attack Wi-Fi networks or stored Wi-Fi passwords.

---

## Intern Details

- **Intern ID:** CITS8842
- **Full Name:** KOLA TEJAS
- **No. of Weeks:** 8 Weeks
- **Project Name:** Wi-Fi Password Security Auditor
- **Project Scope:** Cybersecurity / Ethical Hacking

---

## Objectives

- Check the security strength of a Wi-Fi password.
- Evaluate password length and character diversity.
- Identify common password security weaknesses.
- Provide suggestions for creating stronger passwords.
- Demonstrate basic Python programming and cybersecurity concepts.

---

## Features

- Password length analysis.
- Uppercase letter detection.
- Lowercase letter detection.
- Number detection.
- Special character detection.
- Common weak password detection.
- Security score calculation.
- Weak, Medium, or Strong classification.
- Password improvement suggestions.
- Simple command-line interface.

---

## Technologies Used

- Python
- Regular Expressions (`re`)
- Python Standard Library

---

## Project Files

```text
WiFi-Password-Security-Auditor/
│
├── wifi_password_auditor.py
├── README.md
└── requirements.txt
```

---

## Requirements

Python 3.x is recommended.

No external Python packages are required.

The project uses Python's built-in `re` module.

---

## How to Run

### Option 1: Run Locally

1. Download or clone this repository.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the following command:

```bash
python wifi_password_auditor.py
```

5. Enter the Wi-Fi password you want to audit.
6. The program will display the security score, security level, and suggestions.

---

## Option 2: Run Using an Online Python Compiler

The project can also be tested using an online Python compiler without installing Python.

### Steps:

1. Open an online Python compiler such as **Programiz, OnlineGDB, or Replit**.
2. Open `wifi_password_auditor.py` from this GitHub repository.
3. Copy the complete Python source code.
4. Paste the code into the online Python editor.
5. Click the **Run** button.
6. Enter a Wi-Fi password when prompted.
7. The program will analyze the password.
8. The program will display the password length, security score, security level, and improvement suggestions.

No external packages need to be installed because the project uses Python's built-in `re` module.

---

## Example Input and Output

### Example Input

```text
=======================================================
           WI-FI PASSWORD SECURITY AUDITOR
=======================================================
Enter Wi-Fi password to audit: Hello
```

### Example Output

```text
=======================================================
           WI-FI PASSWORD SECURITY AUDITOR
=======================================================

Password Security Result
-------------------------------------------------------
Password Length: 5
Security Score: 2 / 6
Security Level: WEAK

Security Suggestions
-------------------------------------------------------
- Use at least 8 characters. 12 or more is recommended.
- Add at least one number.
- Add at least one special character.

=======================================================
Security audit completed.
=======================================================
```

---

## Security Scoring

The auditor checks several password security characteristics:

| Security Check | Score |
|---|---:|
| Password length | Up to 2 points |
| Uppercase letter | 1 point |
| Lowercase letter | 1 point |
| Number | 1 point |
| Special character | 1 point |
| **Maximum Score** | **6 points** |

### Security Levels

- **Strong:** 6 / 6
- **Medium:** 4–5 / 6
- **Weak:** 0–3 / 6

---

## Common Weak Passwords

The program checks for several commonly used weak passwords, including:

```text
password
12345678
123456789
password123
qwerty123
admin123
welcome123
```

Users should avoid easily guessed or commonly used passwords.

---

## Project Scope

This project is designed for educational cybersecurity and ethical hacking purposes.

The tool performs password-strength analysis on a password entered by the user. It does not perform network scanning, password cracking, Wi-Fi attacks, credential extraction, or unauthorized access.

---

## Limitations

- The tool evaluates password characteristics only.
- It does not determine whether a password has been exposed in a data breach.
- It does not connect to or scan Wi-Fi networks.
- It does not retrieve saved Wi-Fi passwords.
- The security score is a basic educational assessment and should not be considered a complete password-security evaluation.

---

## Conclusion

The Wi-Fi Password Security Auditor demonstrates how Python can be used to perform basic cybersecurity password analysis.

The project helps users understand important password security principles such as sufficient length, character diversity, and avoiding common passwords.
