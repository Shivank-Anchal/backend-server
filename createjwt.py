import jwt

class CreateJwt():
    def __init__(self,json_object):
        self.json_object = json_object
        self.encoded_jwt = jwt.encode(self.json_object,'secret',algorithm='HS256')
        pass
    def jwt_created(self):
        return self.encoded_jwt