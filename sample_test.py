
import json


def readFile():
    with open('user_data.json') as f:
        data=json.load(f)
    f.close()
    return data["Users"]


def compare_password(userId,password):
    user_list = readFile()
    for i in range(len(user_list)):
        if(userId==user_list[i]['user'+str(i+1)]['userId']):
            if(user_list[i]['user'+str(i+1)]['password']==password):
                print('password matches')
            else:
                print('password doesnot match')


if __name__=="__main__":
    compare_password('shivank','8994454')