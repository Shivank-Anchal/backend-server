from flask import Flask,jsonify,request
import json
from flask_cors import CORS
from add_user import AddUser
from enquire import Enquire
from user_info import UserInfo
from login import Login

app=Flask(__name__)
CORS(app)

@app.route('/api/authenticate',methods=['POST'])
def post_request():
    if request.method == 'POST':
        #print(request.data)
        user_data_recieved_in_bytes  = request.data
        #decoding bytes to string
        user_data_converted_to_string= convert_bytes_to_string(user_data_recieved_in_bytes)
        #converting string to json
        userInfoJson=json.loads(user_data_converted_to_string)


        user = UserInfo(userInfoJson['email'],userInfoJson['password'])
        
        if(userInfoJson['type']=='login'):
            '''
            initiate userLogin
            result contains result after compleleting userLogin
            '''
            result = userLogin(user)


        else:
            '''
            initiate userSignUp
            result contains result after completing userSignUp
            '''
            result = userSignUp(user)
        print(result)
        return jsonify(result)


    
def registerTheUser(user):
    userId=user.userId
    password=user.password
    '''
    user_enquiry.check_existence_of_user_in_the_register()==True
    user exists
    else 
    does not exists
    '''
    userEntry = AddUser(userId,password)
    result_after_registeration = userEntry.start_registering()
    return result_after_registeration
    


def userLogin(user):
    userId = user.userId
    password = user.password
    user_enquiry = Enquire(userId)
    if(user_enquiry.check_existence_of_user_in_the_register()):
        login = Login(userId,password)
        login.compare_password()
        if(login.does_password_matches()):
            token_in_bytes=login.get_jwt()
            token_in_string=convert_bytes_to_string(token_in_bytes)
            return {
                'result':'login successful',
                'token':token_in_string
            }
        else:
            return {
                'result':'login unsuccessful',
                'reason':'incorrect password'
            }
    else:
        return {
            'result':'login unsuccessful',
            'reason':'userId does not exists'
        }
    
    

    if(login.does_password_matches()):
        return login.get_jwt()
    else:
        return {
            "invalidLogin":True,
            "response":'incorrect password'
            }

def userSignUp(user):
    userId=user.userId
    password=user.password
    user_enquiry = Enquire(userId)
    if(user_enquiry.check_existence_of_user_in_the_register()):
        return {
            'result':'user already exists'
        }
    else:
        if(registerTheUser(user)):
            return {
            'result':'user does not exists,hence registering'
        }
        else:
            return {
                'result':'user not registered, due to server bugs'
            }

def sendJWTToken():
    pass

def convert_bytes_to_string(byte_data):
    return byte_data.decode('utf-8')


if __name__=='__main__':
    app.run(debug=True)