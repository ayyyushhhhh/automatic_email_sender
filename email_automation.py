import stdiomask
import save_data
from send_mail import Mail
data_list = [] 

sender_email = input(" Please Enter your email address : ")
sender_password = stdiomask.getpass(prompt= "Please Enter your password : ")

data_file = input("Please input the csv filename : ")

data_list = save_data.get_data("data_file")


subject = input("Please Enter subject of your mail. : ")  




for data in enumerate(data_list):
    print("Number of emails sent : {}".format(data_list.index(data)))
    mail = Mail()
    mail.add_subject(subject)
    mail.send_mail("smtp.gmail.com", 465, sender_email, sender_password,data)









 



