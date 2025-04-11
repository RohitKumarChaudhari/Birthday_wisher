# 🎂 Birthday Wisher App (Python)

This project automatically sends birthday wishes via email to your friends or family every year. The script reads the birthday data from a `.csv` file, selects a random message template from a folder containing `.txt` files, and sends the message to the respective email address.

---
---

## ⚙️ Features

- Reads birthday data from a CSV file.
- Selects a random message template from a folder.
- Automatically fills in the name and sends an email.
- Runs daily to check and wish anyone whose birthday is today.

---

## 📝 CSV File Format (`birthdays.csv`)

The CSV file must be structured like this:

| name    | email               | year | month | day |
|---------|---------------------|------|-------|-----|
| Rohit   | rohit@email.com     | 2000 | 4     | 11  |
| Ramesh  | ramesh@email.com    | 1998 | 4     | 11  |

---

## 📨 Email Setup

Set up your email credentials using environment variables or directly in the code (not recommended for public repos).

- Enable **"Less secure apps"** or **App Password** for Gmail accounts.
- Example for email setup using `smtplib`:

```python
import smtplib

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user="your_email@gmail.com", password="your_password")
```

## 📦 Requirements  
- Python 3.x  
- pandas  
- smtplib
- datetime  
- random   

```bash
pip install pandas
``` 
## 🚀 How to Run
```bash
python main.py
```
Make sure you have internet access and your email credentials are correct.  



📬 Made with 💙 by Rohit


