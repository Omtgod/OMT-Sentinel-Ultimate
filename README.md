# OMT-Sentinel-Ultimate
Advanced Discord Automation &amp; Analysis Tool for Educational Research. Built with Python and Discord.py. Optimized for high-speed performance and security.
🛡️ OMT-Sentinel Ultimate v1.0
Educational Purposes Only | Use at Your Own Risk

Advanced Discord automation and analysis tool designed for research and educational experiments. This version features secure license verification and a professional command dashboard.

🚀 Installation & Setup
📱 Option A: Mobile Users (Android - Termux)
Step 1: Install Termux

Download Termux from F-Droid (Play Store version is outdated).

Open Termux and paste this command to setup everything at once:
pkg update && pkg upgrade -y && pkg install python git nano -y

Step 2: Clone & Install

Run these commands:
git clone https://github.com/YOUR_GITHUB_USERNAME/OMT-Sentinel-Ultimate
cd OMT-Sentinel-Ultimate
pip install -r requirements.txt

Step 3: Configuration (Very Important)

Run the bot once to generate the config file:
python OMT_Sentinel.py

Now, open the config editor:
nano config.json

Use arrow keys to find these lines and replace the text inside quotes:

"LICENSE_KEY": "YOUR_KEY_HERE"

"DISCORD_TOKEN": "YOUR_ALT_TOKEN_HERE"

"MAIN_ACCOUNT_ID": "YOUR_ID_HERE"

To Save: Press Ctrl + O, then Enter.

To Exit: Press Ctrl + X.

Start the bot again:
python OMT_Sentinel.py

💻 Option B: PC Users (Windows)
Download OMT-Sentinel-v1.0.exe from the Releases section on the right side of this page.

Run the .exe file. It will automatically create a config.json in the same folder.

Open config.json with Notepad, fill in your Token and License Key, and save.

Restart the application to access the Dashboard.

🎮 Commands & Controls
!done: Resume bot after a captcha or manual pause.

!stop: Emergency shutdown of the bot.

⚠️ Legal Disclaimer
This software is strictly for educational purposes only. The developer (@omt_god) is not responsible for any account bans, data loss, or legal issues. Usage of this tool implies acceptance of all risks involved. This tool is hardware/ID locked for security purposes.
---

## 🎮 Commands & Controls
- `!done`: Resume bot after captcha or pause.
- `!stop`: Emergency shutdown.

---

## ⚠️ Legal Disclaimer
This tool is for **educational purposes only**. The developer (@omt_god) is not responsible for any account bans or losses. Usage of this tool implies acceptance of all risks involved.
