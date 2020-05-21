import json

class UserData:
    def __init__(self,user_position_in_list):
        #position starts from 0
        self.user_position_in_list = user_position_in_list
        pass

    def get_user_list(self):
        with open('user_data.json') as f:
            data=json.load(f) 
        f.close
        return data["Users"]
    
    def getUserData(self):
        user_list = self.get_user_list()
        i = self.user_position_in_list
        userData = user_list[i]['user'+str(i+1)]
        return userData