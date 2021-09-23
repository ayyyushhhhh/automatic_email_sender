
import save_data
from send_mail import Mail
data_list = [] 

sender_email = input(" Please Enter your email address")
sender_password = input(" Please Enter your password")

data_list = save_data.get_data("Names.csv")
subject = "Certificate of participation" 

for data in data_list:
    mail = Mail()
    mail.add_subject(subject)
    mail.send_mail("smtp.gmail.com", 465, sender_email, sender_password,data)









 



