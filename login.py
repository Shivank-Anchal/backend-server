import json
from createjwt import CreateJwt
from user_info import UserInfo

class Login():
    def __init__(self,userId,password):
        self.userId = userId
        self.password = password

    def readFile(self):
        with open('user_data.json') as f:
            data=json.load(f)
        f.close()
        return data["Users"]

    def does_password_matches(self):
        return self.password_match


    def compare_password(self):
        user_list = self.readFile()
        for i in range(len(user_list)):
            if(self.userId==user_list[i]['user'+str(i+1)]['userId']):
                if(user_list[i]['user'+str(i+1)]['password']==self.password):
                    self.password_match = True
                else:
                    self.password_match=False

    def get_jwt(self):
        if(self.password_match):
            user_info = UserInfo(self.userId,self.password)
            jwt = CreateJwt(user_info.getUserIdPassword())
            return jwt.jwt_created()

        
