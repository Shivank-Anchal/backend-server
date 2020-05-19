class ToBeRegisteredUser:
    def __init__(self,userId,password):
        self.userId=userId
        self.password=password
    
    def getUserIdPassword(self):
        user={
                "userId" : self.userId,
                "password":self.password
            }
        return user