# 🤖 YouTube Media Downloader Bot for Telegram

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-Media-red?style=for-the-badge&logo=youtube&logoColor=white)

<p align="center">
  <a href="#-english">🇺🇸 Read in English</a> &nbsp;&bull;&nbsp;
  <a href="#-portugês">🇧🇷 Leia em Português</a>
</p>

---

<div id="-english"></div>

## 🇺🇸 English

### 📖 About
High-performance Telegram bot designed to download and manage YouTube content seamlessly. Built using **Python**, **yt-dlp**, and following **Clean Architecture** principles to ensure maintainability and scalability.

### ✨ Features
* Download videos from YouTube directly via Telegram.
* Selectable video quality.
* Fast and efficient media handling.

### 🚀 How to Run

#### 1. Get your API Token
To function, you must create a bot on Telegram via **BotFather**:
1.  Open [BotFather](https://telegram.me/BotFather).
2.  Send the command `/newbot`.
3.  Follow the instructions to get your **HTTP API Token**.

#### 2. Configure the Code
> **Security Note:** Ideally, store tokens in an `.env` file. For this version, follow the manual step below:

1.  Open the file `bot.py`.
2.  Go to **line 6**.
3.  Replace the empty variable `TOKEN = ''` with your token:
    ```python
    TOKEN = 'YOUR_TOKEN_HERE_123456'
    ```

#### 3. Start the Bot
Run the script in your terminal:
```bash
python bot.py
