
Email Status Checker 📧🔍

Description
This Python script helps check whether email usernames (e.g., Yahoo or Gmail) are available or taken. It reads a list of email addresses, sends requests to an API, and categorizes the results into Linked or Not Linked accounts. Perfect for automation tasks related to email verification! 💻✨

Features 🌟
📝 Reads email usernames from a file (email.txt).
🌐 Queries APIs to check the status of emails.
📂 Automatically saves results into:
Linked.txt for Taken accounts.
NotLinked.txt for Available accounts.
🔄 Adjustable sleep interval between requests to avoid overloading the API.
🔒 Uses dynamic user-agent headers for added anonymity.
Installation 🚀
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/email-checker.git
cd email-checker
Install Required Packages
bash
Copy code
pip install requests user-agent
Add the Email List
Create a file named email.txt in the same directory and add your list of emails, one per line.

Usage ⚙️
Run the script:

bash
Copy code
python email_checker.py
Enter the sleep interval (e.g., 2 seconds):

plaintext
Copy code
sleep: 2
Output Files 🗂️
Linked.txt: Contains emails that are taken.
NotLinked.txt: Contains emails that are available.
Preview 📸
kotlin
Copy code
███████╗███╗   ███╗ █████╗ ██╗██╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
██╔════╝████╗ ████║██╔══██╗██║██║     ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
█████╗  ██╔████╔██║███████║██║██║     ██║     ███████║█████╗  ██║     █████╔╝ 
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
by @Makavael +201029107547
Warnings & Limitations ⚠️
Educational Use Only: This script is designed for research and learning purposes.
Ethical Use: Avoid any misuse, such as violating terms of service or overloading servers.
Ensure you have permission to test the provided APIs and email addresses.
License 📜
This project is open-source under the MIT License. Use responsibly.

Contact ✉️
Author: Makavael
WhatsApp: +201029107547
Website: www.Makavael.com
