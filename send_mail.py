import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from data_model import Data

class Mail:
    def __init__(self):
        self.message = MIMEMultipart("alternative") 
        

    def add_attachment(self,file_name):

        with open(file_name,"rb") as file:
            part = MIMEBase("application","octet-stream")
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename = {file_name}")
            self.message.attach(part)
           
    
    def __message_body(self,name=None):
        return "Hi {}, Please find the attachment in the mail".format(name)
    

    def add_subject(self,sub:str):
        self.message["Subject"] = sub
    

    def add_body(self,name=None):
        
        body =MIMEText(self.__message_body(name),_subtype='plain', _charset='UTF-8')
        self.message.attach(body)
     


    def send_mail(self,connection_name:str,connection_number:int
    , sender_email : str ,sender_password : str,reciever:Data  ):

        context = ssl.create_default_context()

        # create server connection
        with smtplib.SMTP_SSL(connection_name,connection_number,context) as server:
            server = smtplib.SMTP_SSL(connection_name,connection_number)
            # loging to the to the server 
            try:
                server.login(sender_email, sender_password)
            except smtplib.SMTPAuthenticationError:
                print("Wrong Password ") 
                return
            else:
                print("Unknown Error Occured")

            # adding reciever message
            self.message["To"] = reciever.email

            # add message to the message body
            self.add_body(reciever.name)

            #add attachment
            self.add_attachment(f"{reciever.name}.pdf")

            #convert message object to string as the sendmail takes string as input
            self.message = self.message.as_string()

            # send mail 
            server.sendmail(sender_email,reciever.email, self.message)

            # quit server
            server.quit()

      