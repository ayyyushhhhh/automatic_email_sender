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
        pass


    def send_mail(self,connection_name:str,connection_number:int
    , sender_email : str ,sender_password : str,reciever:Data  ):

        context = ssl.create_default_context()

        # create server connection
        with smtplib.SMTP_SSL(connection_name,connection_number,context) as server:
            server = smtplib.SMTP_SSL(connection_name,connection_number)
            # loging to the to the server 
            try:
                server.login(sender_email, sender_password)
            except:
                print("unknown Error Occured") 
                return

            print("sending please, wait...")
            self.message["To"] = reciever.email
            self.add_body(reciever.name)
            self.add_attachment(f"{reciever.name}.pdf")
            self.message = self.message.as_string()
            # send mail 
            server.sendmail(sender_email,reciever.email, self.message)
            # quit server
            server.quit()

            print("All Emails sent.., have a nice day")
