Mailx 📧
A powerful email status checker script by Makavael 🚀


Features 🌟
🔍 Check the availability of Yahoo and Gmail usernames.
📝 Automatically saves results to Linked.txt (Taken) and NotLinked.txt (Available).
🌐 Uses API requests with dynamic User-Agent headers.
⏱️ Adjustable delay between requests to prevent API overload.
Installation 🚀
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Mailx.git
cd Mailx
Install dependencies:

bash
Copy code
pip install requests user-agent
Add your email list:

Create a file named email.txt in the same directory and add emails (one per line).
Usage ⚙️
Run the script:

bash
Copy code
python emailcheck.py
Input sleep interval:
Adjust the delay (in seconds) between API requests to avoid overloading. Example:

plaintext
Copy code
sleep: 2
Output Files:

Linked.txt: Contains emails that are taken.
NotLinked.txt: Contains emails that are available.
Output Example
scss
Copy code
test1@yahoo.com: Taken[!]
test2@gmail.com: Available[*]
Preview 📸
csharp
Copy code
███████╗███╗   ███╗ █████╗ ██╗██╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
██╔════╝████╗ ████║██╔══██╗██║██║     ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
█████╗  ██╔████╔██║███████║██║██║     ██║     ███████║█████╗  ██║     █████╔╝ 
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
         Created by Makavael | WhatsApp: +201029107547
Disclaimer ⚠️
This script is for educational purposes only. Using this tool for unauthorized purposes is a violation of the law and ethical guidelines. Please ensure you have permission to test email availability.

Author ✉️
Makavael
WhatsApp: +201029107547
Website: www.Makavael.com
