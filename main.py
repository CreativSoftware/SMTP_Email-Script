import smtplib
import datetime as dt
import random


current_time = dt.datetime.now()
weekday = current_time.weekday()

if weekday == 0:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        quote_choice = random.choice(quotes_list)
        
    sender_email = "competitionmatrix@gmail.com"
    password = "123456"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email, 
            to_addrs="creativematrix1@gmail.com", 
            msg=f"Subject: Quote of the Day!\n\n{quote_choice}\n\nEdward Perry"
        )



