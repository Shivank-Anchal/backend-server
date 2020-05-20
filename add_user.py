import json
from user_info import UserInfo

class AddUser():
    def __init__(self,userId,password):
        self.userId=userId
        self.password=password

    def start_registering(self):
        #recievng user info in json form
        new_user = self.getUserInfo()
        user_list_append_new_user = self.append_json_to_list(self.readFile(),new_user)
        self.writeFile(user_list_append_new_user)

    def writeFile(self,data):
        file_to_be_written = {
            "Users":data
            }
        with open('user_data.json','w+',encoding='utf-8') as f:
            json.dump(file_to_be_written,f,indent=4)
        f.close()
        return True

    def append_json_to_list(self,users_list,new_user_data):
        #convert  json_object to list 
        #Add json_objet_list to users_list
        length_of_list = len(users_list)
        json_object={
            "user"+str(length_of_list+1):new_user_data
        }
        return (users_list + [json_object])

    def getUserInfo(self):
        new_user = UserInfo(self.userId,self.password)
        return new_user.getUserIdPassword()

    def readFile(self):
        with open('user_data.json') as f:
            data=json.load(f)
        f.close()
        return data["Users"]
        



