# Advanced Python Keylogger (For Ethical Hacking Demonstration)

> **⚠️ Ethical Use Only:** This project is intended **only for educational and ethical testing purposes**. Using this tool on systems without consent is illegal and unethical.

---

## 📌 Project Overview
This is an advanced Python keylogger created for simulating real-world attack scenarios in a controlled environment. The script logs keystrokes, captures screenshots, gathers system information, and sends the logs to a configured email at regular intervals — all in stealth mode.

---

## 🎯 Features
- Stealth mode keylogger
- Captures keystrokes
- Takes automatic screenshots
- Logs system and IP details
- Sends logs via email every 5 minutes
- Background execution ready (convert to .exe for Windows)

---

## 🧰 Requirements
Install required libraries using pip:

pip install pynput pillow requests

---

## 📂 Project Structure
```
advanced_keylogger_project/
├── advanced_keylogger.py          # Main script
├── email_config.py                # Your email credentials (DO NOT upload this publicly)
├── .keylogs/                      # Logs and screenshots folder
└── README.md                      # This file
```

---

## 🛠️ Setup Instructions

### 1. Configure Email Credentials
Create a file named `email_config.py`:
```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "receiver_email@gmail.com"
```
> **Note:** Use an App Password if you're using Gmail. Enable "Less secure apps" or generate an app password for Gmail 2FA accounts.

### 2. Run the Keylogger

python advanced_keylogger.py


### 3. Convert to Executable (Windows Only)

pip install pyinstaller
pyinstaller --noconsole --onefile advanced_keylogger.py
```
This will generate an `.exe` file inside the `dist/` folder.

---

## 🔍 How It Works
- The script listens to all keystrokes using `pynput`.
- Every 5 minutes, it:
  - Saves typed keys to a text file
  - Takes a screenshot using `Pillow`
  - Gathers system info like hostname, IP, platform
  - Emails the log and screenshot as attachments

---

## 🚀 Use Case (Ethical)
This project helps cybersecurity students and professionals understand how attackers may use keyloggers, thereby helping in designing better defenses and monitoring mechanisms. It is suitable for demo, awareness, and educational environments.

---

## ❗ Legal & Ethical Disclaimer
This tool is developed solely for **ethical and educational purposes**. Do **not use** this software to monitor or collect data from systems you do not own or have explicit permission to test. Unauthorized usage is a criminal offense and punishable by law.

---

## 📌 Future Enhancements
- Encrypt log files before sending
- Cloud storage integration (Google Drive/Dropbox)
- GUI dashboard for log review

---

## 🧠 Author
Created by **Yash Khedkar** for ethical cybersecurity project demonstrations.

GitHub: [yashkhedkar087]

---

Stay ethical. Stay secure. 🛡️

