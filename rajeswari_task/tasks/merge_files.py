
file_1=r"C:\Users\YasodhaS-3242\PycharmProjects\PythonProject\rajeswari_task\files\file_1.txt"
file_2=r"C:\Users\YasodhaS-3242\PycharmProjects\PythonProject\rajeswari_task\files\file_2.txt"
file_3=r"C:\Users\YasodhaS-3242\PycharmProjects\PythonProject\rajeswari_task\files\mail_file.txt"

with open(file_1,"r")as f1, open(file_2,"r") as f2:
    read_1=f1.read()
    read_2=f2.read()

    merge_mail=read_1 + "\n------------------------\n" + read_2

with open(file_3,"w") as f3:
    f3.write(merge_mail)

########################################################################################

import os
import smtplib
from email.message import EmailMessage

email_id = 'yasodhareddy432@gmail.com'
email_pass = "swfk ymph wmda jsgv"

msg = EmailMessage()

recipient_list = ["bharathredd6@gmail.com", "kushalans9121@gmail.com", "user123@gmail.com" ]
msg['Subject'] = 'first mail using python'
msg['From'] = email_id
msg['To'] = recipient_list  # email_id

msg.set_content('Hello.!! every one.. \n \nThis is auto-generated mail.... \n \nIgnore this mail   \n \nThanks & Regards \n Yasodha')
for each_file in os.listdir():
    if each_file == "mail.py":
        continue
    with open(each_file, "rb") as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)


############################################################################


"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("yasodhareddy432@gmail.com", "8546918905")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("you@gmail.com", "target@example.com", msg)