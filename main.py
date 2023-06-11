import smtplib
import pandas
from datetime import datetime
from random import randint


MY_EMAIL = "zanechan136@gmail.com"
PASSWORD = "lxikjnaxdqgvykpp"
BIRTHDAYS_FILE = "./birthdays.csv"
NUMBER_OF_TEMPLATES = 3

# get the current day to check if its birthday
current_date = (datetime.now().month, datetime.now().day)

# read .csv file and create new dictionary
data = pandas.read_csv(BIRTHDAYS_FILE)
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

if current_date in birthdays_dict:
    template_num = randint(1, NUMBER_OF_TEMPLATES)
    file_path = f"./letter_templates/letter_{template_num}.txt"
    birthday_person = birthdays_dict[current_date]

    try:
        with open(f"./letter_templates/letter_{template_num}.txt") as letter:
            contents = letter.read()
            contents = contents.replace("[NAME]", birthday_person["name"])
    except FileNotFoundError:
        print("Error: Birthdays File Not Found. Please, create birthdays.csv file.")
    else:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}."
            )
