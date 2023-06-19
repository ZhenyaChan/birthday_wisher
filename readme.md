# Birthday Wisher Program

## Description
- Implementation of the Birthday Wisher Program using latest technologies of <strong>OOP concepts, Python, 
Pandas Data Analysis Library, random, datetime, and smtplib modules</strong>.
- The program helps users to send happy birthday emails to their friends based on their date of birth in `birthdays.csv` file. 
- The program compares the birthdays list of each person from .csv file with current date, and selects random template 
from `letter_templates` folder, puts person name, and sends it using SMTP protocol client.

## How to Setup the Project
1. Create an empty folder
2. Add the folder to workplace area in your VS Code and open terminal OR navigate to the created folder using terminal
3. Download the project .zip file OR Enter to the terminal:
   `git clone https://github.com/ZhenyaChan/birthday_wisher.git`
4. Change <strong>MY_EMAIL, PASSWORD</strong> variables to your email and app password in profile settings.
5. Run the code by entering in the terminal `python3 "./main.py`
```sh
NOTE: If the email of the recipient is not @gmail, you have to change smtp address:
Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com
```
