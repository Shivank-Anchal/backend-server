import json
from userRegister import ToBeRegisteredUser

def writeFile(data):
    with open('user_data.json','w+',encoding='utf-8') as f:
        json.dump(data,f,indent=4)

def append_json_to_list(users_list,new_user_data):
    #convert  json_object to list 
    #Add json_objet_list to users_list
    length_of_list = len(users_list)
    json_object={
        "user"+str(length_of_list+1):new_user_data
    }
    return (users_list + [json_object])

def getUserInfo():
    new_user = ToBeRegisteredUser(input('userId     '),input('password      '))
    data=readFile()
    return new_user.getUserIdPassword()

def readFile():
    with open('user_data.json') as f:
        data=json.load(f)

    return data

def start():
    data=readFile()
    new_user = getUserInfo()
    value=check_existance_of_user(new_user,data['Users'])
    if(value==False):
        data["Users"]=append_json_to_list(data["Users"],new_user)
        writeFile(data)
    
def check_existance_of_user(userData,users_list):
    value=False
    for i in range(len(users_list)):
        if(userData['userId']==users_list[i]['user'+str(i+1)]['userId']):
            print('userId already exist')
            value=True
            break
    return value

if __name__=="__main__":
    start()



