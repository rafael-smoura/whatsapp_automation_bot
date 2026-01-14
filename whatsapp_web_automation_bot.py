"""
============================================================
WHATSAPP WEB AUTOMATION BOT (NON-OFFICIAL API)
============================================================

INSTALLATION AND EXECUTION GUIDE

1. SYSTEM REQUIREMENTS
------------------------------------------------------------
- Windows 10 or newer
- Python 3.10 or newer
- Google Chrome installed
- XAMPP (Apache and MySQL)

2. DEPENDENCY INSTALLATION
------------------------------------------------------------
Ensure the file "requirements.txt" exists in the project root with the following content:

selenium>=4.10.0
requests>=2.31.0

Install all dependencies using the command:

pip install -r requirements.txt

3. BACKEND CONFIGURATION (PHP)
------------------------------------------------------------
- Start XAMPP
- Enable Apache and MySQL services
- Place the PHP backend file at:

C:\xampp\htdocs\bot\index.php

- The bot communicates with the PHP backend via HTTP.
- DO NOT modify the PHP communication logic.

4. MYSQL DATABASE SETUP
------------------------------------------------------------
Before running the bot, you must create the MySQL database and tables required by the PHP backend.

1. Open phpMyAdmin (http://localhost/phpmyadmin/) or MySQL CLI.
2. Create the database `bot`.
3. Create the `usuario` table with columns:
   - id INT AUTO_INCREMENT PRIMARY KEY
   - telefone VARCHAR(20) NOT NULL
   - status INT DEFAULT 1
4. Create the `historico` table with columns:
   - id INT AUTO_INCREMENT PRIMARY KEY
   - telefone VARCHAR(20)
   - msg_cliente TEXT
   - msg_bot TEXT
   - data DATETIME

> ⚠️ Make sure the MySQL service is running and the database/tables exist before running the bot.

5. SESSION STORAGE
------------------------------------------------------------
- The WhatsApp Web session is stored locally to avoid repeated QR Code scans.
- Session directory used by this bot:

storage/whatsapp_session

6. FIRST EXECUTION
------------------------------------------------------------
- Run the script:

python whatsapp_web_automation_bot.py

- Scan the WhatsApp Web QR Code if requested.
- Keep the browser open while the bot is running.

7. BOT OPERATION
------------------------------------------------------------
- Automatically monitors unread WhatsApp messages
- Opens the most recent unread conversation
- Sends received messages to the PHP backend
- Receives and sends automated responses
- Designed for professional and commercial use

IMPORTANT NOTES
------------------------------------------------------------
- This bot uses WhatsApp Web (non-official API)
- Use responsibly and in accordance with WhatsApp policies
- Do not close the browser during execution

============================================================
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import requests

# -----------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------

BOT_USER_EMAIL = "example@gmail.com"
HTTP_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# Confirmed working class for unread message indicator
UNREAD_BADGE_CLASS = "_ahlk"

# Stable selectors
MESSAGE_INPUT_SELECTOR = '//div[@contenteditable="true"][@data-tab="10"]'
CHAT_HEADER_NAME_SELECTOR = '//*[@id="main"]/header//span[@dir="auto"]'

# Session storage directory
BASE_DIR = os.getcwd()
SESSION_DIR = os.path.join(BASE_DIR, "storage", "whatsapp_session")

chrome_options = Options()
chrome_options.add_argument(r"user-data-dir=" + SESSION_DIR)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 20)

print("=================================================")
print(" WHATSAPP AUTOMATION BOT SUCCESSFULLY INITIALIZED ")
print(" Monitoring incoming messages...")
print(f" Unread indicator class: {UNREAD_BADGE_CLASS}")
print("=================================================")

# -----------------------------------------------------------
# BOT CORE FUNCTION
# -----------------------------------------------------------

def bot():
    try:
        # 1. Locate unread message indicators
        unread_badges = driver.find_elements(By.CLASS_NAME, UNREAD_BADGE_CLASS)

        if not unread_badges:
            return

        # 2. Open the most recent unread chat
        latest_badge = unread_badges[-1]
        ActionChains(driver)\
            .move_to_element_with_offset(latest_badge, 0, -20)\
            .click()\
            .perform()

        time.sleep(1.5)

        # 3. Retrieve client name or phone number
        client_info = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, CHAT_HEADER_NAME_SELECTOR)
            )
        ).text

        # 4. Retrieve the last incoming message
        incoming_messages = driver.find_elements(
            By.XPATH,
            '//div[contains(@class, "message-in")]//span[contains(@class, "selectable-text")]'
        )

        received_text = incoming_messages[-1].text if incoming_messages else "Hello"

        print(f"New interaction detected | Client: {client_info} | Message: {received_text}")

        # 5. PHP backend communication (DO NOT MODIFY LOGIC)
        try:
            php_url = "http://localhost/bot/index.php"
            params = {
                "telefone": client_info,
                "msg": received_text,
                "usuario": BOT_USER_EMAIL
            }

            response = requests.get(php_url, params=params, timeout=10)
            php_reply = response.text.strip()

        except Exception as error:
            print(f"Backend communication error: {error}")
            return

        # 6. Send response through WhatsApp
        if php_reply:
            message_box = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, MESSAGE_INPUT_SELECTOR)
                )
            )

            message_box.click()
            time.sleep(0.5)
            message_box.send_keys(php_reply + Keys.ENTER)

            print(f"Automated response successfully sent to {client_info}")

        # 7. Close chat to refresh view
        time.sleep(1)
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    except Exception:
        # Silent failure to maintain continuous execution
        pass

# -----------------------------------------------------------
# MAIN LOOP
# -----------------------------------------------------------

while True:
    bot()
    time.sleep(2)
