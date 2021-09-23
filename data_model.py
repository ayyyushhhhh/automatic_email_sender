class Data:
    def __init__(self,name,email,attachment = None, subject= "", body= ""):
        self.name = name
        self.email = email 
        self.subject = subject
        self.body = body
        self.attachment = attachment