# 🤖 WhatsApp Web Automation Bot (Unofficial API)

> Python + Selenium automation for WhatsApp Web with a PHP & MySQL backend.

⚠️ **Disclaimer**  
This project does **NOT** use the official WhatsApp API.  
It automates WhatsApp Web through browser interaction and is intended for **educational, experimental, or internal business use only**.  
Use responsibly and **at your own risk** — WhatsApp may restrict or ban automated accounts.

---

## 📌 Overview

This project is an **unofficial WhatsApp Web automation bot** built with **Python (Selenium)** and integrated with a **PHP backend** and **MySQL database**, running locally via **XAMPP**.

The bot monitors unread messages on WhatsApp Web, captures incoming messages, sends them to a PHP endpoint for processing, and automatically replies — all without using the official WhatsApp API.

This project was developed as a **learning-by-building experiment**, focusing on automation, backend integration, browser-based interaction, and real-world problem solving.

---

## 🧠 How It Works

### Python (Selenium)
- Opens WhatsApp Web using Google Chrome  
- Detects unread messages using DOM selectors  
- Opens the most recent unread conversation  
- Extracts the last received message  
- Sends message data to the PHP backend via HTTP  

### PHP Backend
- Receives message data via HTTP (GET)  
- Processes logic using MySQL  
- Returns a response string  

### Automated Response
- Python receives the backend response  
- Automatically sends the reply back through WhatsApp Web  

---

## 🛠️ Technologies Used

- Python 3.10+  
- Selenium WebDriver  
- Google Chrome  
- PHP 7+  
- MySQL  
- XAMPP (Apache + MySQL)  
- Requests (Python HTTP library)  
- WhatsApp Web  

---

## 📂 Project Structure

```
.
├── whatsapp_web_automation_bot.py          # Main Python automation script
├── index.php                               # PHP backend (message processing)
├── storage/
│   └── whatsapp_session/                   # Chrome session files (keeps WhatsApp logged in)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation and Execution Guide

### 1. System Requirements

- Windows 10 or newer  
- Python 3.10 or newer  
- Google Chrome installed  
- XAMPP (Apache and MySQL)  

---

### 2. Dependency Installation

Create a `requirements.txt` file in the project root with the following content:

```
selenium>=4.10.0
requests>=2.31.0
```

Install all dependencies using:

```
pip install -r requirements.txt
```

---

### 3. Backend Configuration (PHP)

1. Start **XAMPP**  
2. Enable **Apache** and **MySQL**  
3. Place the PHP backend file at:

```
C:\xampp\htdocs\bot\index.php
```

The bot communicates with the PHP backend via HTTP.  
**Do not modify the PHP communication logic unless strictly necessary.**

---

### 4. MySQL Database Setup

Before running the bot, create the MySQL database and required tables.

Create the database:

```
CREATE DATABASE bot;
```

Create the `usuario` table:

```
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefone VARCHAR(20) NOT NULL,
    status INT DEFAULT 1
);
```

Create the `historico` table:

```
CREATE TABLE historico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefone VARCHAR(20),
    msg_cliente TEXT,
    msg_bot TEXT,
    data DATETIME
);
```

⚠️ Ensure that the MySQL service is running and that the database and tables exist before starting the bot.

---

### 5. Session Storage

The WhatsApp Web session is stored locally to avoid repeated QR code scans.

Session directory:

```
storage/whatsapp_session
```

Do not delete this folder unless you want to reset the WhatsApp login.

---

### 6. First Execution

Run the script:

```
python whatsapp_web_automation_bot.py
```

- Scan the WhatsApp Web QR code if prompted  
- Keep the browser open while the bot is running  

---

## 🔄 Bot Operation

Once running, the bot will:

- Monitor unread WhatsApp messages automatically  
- Open the most recent unread conversation  
- Capture incoming messages  
- Send messages to the PHP backend  
- Receive and send automated responses  
- Run continuously until manually stopped  

---

## 📝 Important Notes

- This bot uses **WhatsApp Web (non-official API)**  
- Automating WhatsApp Web may violate WhatsApp policies  
- Intended for **educational, experimental, or internal business use**  
- Do **not** close the browser while the bot is running  
- WhatsApp Web DOM changes may require selector updates  

---

## ⚡ Troubleshooting

- **Unread messages not detected**  
  Check the unread message badge class in the Python script  

- **Messages not sent**  
  Verify the message input selector  

- **Backend errors**  
  Ensure Apache and MySQL are running  
  Confirm that the database and tables exist  

- **Browser issues**  
  Ensure ChromeDriver matches your Chrome version  

---

## 👨‍💻 Author

**Rafael Moura**  
Computer Engineering Student (UFPE / CIN)

- Python Developer  
- Networking & Cybersecurity Background  
- Content Creator — **Fala Binário**  

🔗 All social links available via ** [**Linktree**](https://linktr.ee/rafael.smoura.dev)**  
💡 Feel free to explore, collaborate, or leave suggestions!
