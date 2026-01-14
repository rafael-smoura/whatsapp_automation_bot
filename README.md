# 🤖 WhatsApp Automation Bot (Unofficial)

> ⚠️ **Disclaimer**  
> This project does **NOT** use the official WhatsApp API.  
> It automates **WhatsApp Web** via browser interaction and is intended **for educational, experimental, or internal business purposes only**.  
> Use responsibly and at your own risk.

---

## 📌 Overview

This project is a **WhatsApp automation bot** built with **Python + Selenium**, integrated with a **PHP backend** and **MySQL**, running locally via **XAMPP**.

The bot monitors unread messages on **WhatsApp Web**, captures incoming messages, sends them to a local PHP endpoint for processing, and automatically replies to the user — all without using the official WhatsApp API.

---

## 🧠 How It Works

1. **Python (Selenium)**  
   - Opens WhatsApp Web using Google Chrome  
   - Detects unread messages via DOM elements  
   - Reads the last received message  
   - Sends message data to a local PHP server  

2. **PHP (index.php)**  
   - Receives data via HTTP (`GET`)  
   - Processes the message using database logic  
   - Returns a response string  

3. **Python Bot**  
   - Receives the PHP response  
   - Automatically sends the reply back on WhatsApp  

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Selenium WebDriver**
- **Google Chrome**
- **PHP 7+**
- **MySQL**
- **XAMPP (Apache + MySQL)**
- **WhatsApp Web**
- **Requests library** for HTTP communication

---

## 📂 Project Structure

```bash
.
├── whatsapp_bot.py     # Main Python bot (Selenium automation)
├── index.php           # PHP backend (message processing)
├── storage/
│   └── whatsapp_session/ # Chrome session files to maintain WhatsApp login
└── README.md

⚙️ Installation & Setup
1. System Requirements

Windows 10 or newer

Python 3.10+

Google Chrome installed

XAMPP (Apache + MySQL)

2. Python Dependencies

Ensure you have a requirements.txt in the project root:

selenium>=4.10.0
requests>=2.31.0


Install dependencies:

pip install -r requirements.txt

3. PHP Backend

Start XAMPP

Enable Apache and MySQL

Place index.php in:

C:\xampp\htdocs\bot\index.php


Do not modify the PHP communication logic unless necessary.

4. MySQL Database Setup

Before running the bot, create the MySQL database and tables required by the PHP backend:

Open phpMyAdmin (http://localhost/phpmyadmin/) or MySQL CLI.

Create the database:

CREATE DATABASE bot;


Create the usuario table:

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefone VARCHAR(20) NOT NULL,
    status INT DEFAULT 1
);


Create the historico table:

CREATE TABLE historico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefone VARCHAR(20),
    msg_cliente TEXT,
    msg_bot TEXT,
    data DATETIME
);


⚠️ Ensure MySQL is running and the tables exist before starting the bot.

5. Session Storage

The bot stores the WhatsApp Web session locally to avoid scanning the QR code every time.

Session folder: storage/whatsapp_session

6. First Execution

Run the bot:

python whatsapp_bot.py


Scan the QR Code on WhatsApp Web if prompted.

Keep the browser open while the bot is running.

📝 Notes & Best Practices

Do not close the browser while the bot is running.

Do not share your WhatsApp credentials; the bot only uses your current session.

Respect WhatsApp's policies — this is intended for internal or experimental use only.

Logs are printed to the console for monitoring activity.

🔄 Bot Operation

Automatically monitors unread WhatsApp messages

Opens the most recent unread conversation

Sends messages to the PHP backend for processing

Sends automated replies back to the user

⚡ Troubleshooting

If messages are not being detected, check the unread message class in whatsapp_bot.py (UNREAD_BADGE_CLASS) — WhatsApp Web DOM changes occasionally.

Ensure MESSAGE_INPUT_SELECTOR matches the current WhatsApp Web input field.

Verify the MySQL database and tables exist and are accessible.

Make sure ChromeDriver is compatible with your Chrome version.

📌 Disclaimer

This bot does not use the official WhatsApp API.
Automating WhatsApp Web carries risk of account restriction.
Use responsibly and at your own risk.