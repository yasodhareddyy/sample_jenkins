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

# for each_file in os.listdir():
#     if each_file == "mail.py":
#         continue
#     with open(each_file, "rb") as f:
#         file_data = f.read()
#         file_name = f.name
#         msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)

