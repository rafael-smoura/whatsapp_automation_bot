
<p align="center">
  <img src="https://github.com/user-attachments/assets/fe96ecfa-36ee-488d-b98e-988e27340091" alt="WhatsApp Automation Bot" width="180">
</p>

<h1 align="center">
  WhatsApp Web Automation Bot
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/language-Python-blue?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/backend-PHP%20%7C%20MySQL-purple?style=flat-square&logo=php&logoColor=white" alt="PHP MySQL" />
  <img src="https://img.shields.io/badge/automation-Selenium-green?style=flat-square&logo=selenium&logoColor=white" alt="Selenium" />
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="MIT License" />
</p>

> ⚠️ **Disclaimer:** This project does **NOT** use the official WhatsApp API. It automates WhatsApp Web through browser interaction and is intended for **educational, experimental, or internal business use only**. Use responsibly and at your own risk — WhatsApp may restrict or ban automated accounts.

---

## 🎯 The Motivation Behind the Project

Customer service automation is one of the most demanded solutions in the modern market, yet access to official business communication APIs often comes with high monthly costs and strict bureaucratic approval barriers. For small businesses, independent developers, or students trying to prototype an interactive system, these restrictions make experimentation nearly impossible.

To bridge this gap and explore the boundaries of browser automation, I developed this unofficial WhatsApp Web bot. Built as a **learning-by-building experiment**, the project challenges the traditional limits of web scrapers by creating a fast, real-time bridge between a standard frontend web application and a traditional relational database infrastructure. It serves as a proof of concept showing how standard engineering tools can solve communication automation bottlenecks with zero budget.

---

## 🚀 Features

* **Real-time DOM Monitoring:** Leverages Selenium selectors to continuously listen to incoming unread message badges without polling crashes.
* **Persistent Session Management:** Implements local Chrome profile caching (`whatsapp_session`) to bypass redundant, repetitive QR code authentication scans.
* **Decoupled Architecture:** Communication relies on an independent backend pipeline, separating automation routines from heavy database CRUD queries.
* **Full Conversation History:** Automatically logs incoming client queries and corresponding machine responses with precise timestamps.

---

## 🧰 Architecture & Components

<table width="100%">
  <tr>
    <td width="120px" align="center" style="border: none;">
      <img src="https://skillicons.dev/icons?i=python,selenium" />
    </td>
    <td style="border: none; padding-left: 15px;">
      <strong>Automation Engine (Python & Selenium):</strong> Handles browser runtime execution, orchestrates DOM state changes, extracts message payloads, and pushes string variables to HTTP endpoints via the <code>requests</code> library.
    </td>
  </tr>
  <tr>
    <td width="120px" align="center" style="border: none;">
      <img src="https://skillicons.dev/icons?i=php,mysql" />
    </td>
    <td style="border: none; padding-left: 15px;">
      <strong>Backend & Storage (PHP & MySQL via XAMPP):</strong> Implements simple, fast business-logic processing via Apache streams, tracking user interaction states and executing analytical sorting queries.
    </td>
  </tr>
</table>

---

## 📦 How to Setup and Run

### 1. Repository & Dependencies Setup
Clone the repository and install the standard execution packages:
```bash
git clone [https://github.com/rafael-smoura/whatsapp-web-automation-bot.git](https://github.com/rafael-smoura/whatsapp-web-automation-bot.git)
cd whatsapp-web-automation-bot
pip install -r requirements.txt
```

## 2. XAMPP Backend Configuration
Ensure XAMPP is active with Apache and MySQL instances running. Deploy the backend entry file to your local server root:
```
C:\xampp\htdocs\bot\index.php
```
## 3. Database Schema Migration
Run the following relational query stream inside your MySQL coordinator or phpMyAdmin environment to initialize core data tracking:
```
CREATE DATABASE bot;
USE bot;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefone VARCHAR(20) NOT NULL,
    status INT DEFAULT 1
);

CREATE TABLE historico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefone VARCHAR(20),
    msg_cliente TEXT,
    msg_bot TEXT,
    data DATETIME
);
```
## 4. First Execution
Launch the Python monitor controller:
```
python whatsapp_web_automation_bot.py
```
📲 Operational Note: Scan the WhatsApp Web QR code on the browser window that pops up. Keep the automated Chrome window open during runtime to preserve active session listeners.

### 🔮 Future Roadmap

The system is engineered as an adaptable base framework. Future releases will focus on reliability and feature-parity with commercial apps:

- [ ] **Dynamic XPath Mutation Shield:** Implement fallback element-finding loops to mitigate breaking runtime errors caused by unexpected layout deployments on WhatsApp Web.
- [ ] **Multi-Agent Router:** Expand the PHP handler to route user tickets based on keyword triggers, enabling multiple bot characters to respond.
- [ ] **Media Attachment Support:** Integrate automation steps to detect, download, and reply using image attachments, audio files, and structural PDFs.

---

## 🌎 Connect With Me

<p align="left">
  <a href="https://linktr.ee/rafael.smoura.dev">
    <img alt="Linktree" src="https://custom-icon-badges.demolab.com/badge/-Linktree-green?style=for-the-badge&logo=linktree&logoColor=white"/>
  </a>&nbsp;
  <a href="https://github.com/rafael-smoura">
    <img alt="GitHub" src="https://custom-icon-badges.demolab.com/badge/-GitHub-black?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

---

<p align="center">
  <b>💡 Developed with purpose.</b><br>
  Engineering software means building solutions that resolve technical roadblocks while positively impacting human experiences.
</p>

<p align="center">
  <sub>Animated icon by <a href="https://www.flaticon.com/free-animated-icons/email" title="email animated icons">Flaticon</a></sub>

