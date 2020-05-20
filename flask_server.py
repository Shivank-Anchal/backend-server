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
        user_data_recieved_in_bytes  =request.data
        #decoding bytes to string
        user_data_converted_to_string= convert_bytes_to_string(user_data_recieved_in_bytes)
        #converting string to json
        userInfoJson=json.loads(user_data_converted_to_string)

        user = UserInfo(userInfoJson['email'],userInfoJson['password'])

        
        '''
        Register the user if does not exist
        result = False if user already exists
        result = True if user is registered
        '''
        result_after_initiating_user_registration = registerTheUser(user)
        print("=======>>>",result_after_initiating_user_registration)
        '''
        We need to check whether the password correct or not
        if password and userid is correct provide JWT 
        else login denied
        '''
        if(result_after_initiating_user_registration.check_existence_of_user_in_the_register()==False):
            print('user is registered')
            return jsonify({
                "response":"user is registered",
                "Existence_of_user":False
            })
        else:
            print('user already exists')
            print(userLogin(user))
            token = convert_bytes_to_string(userLogin(user))
            print(token)

            return jsonify({
                "response":"user already exists",
                "Existence_of_user":True,
                "Token": token
            })


    
def registerTheUser(user):
    userId=user.userId
    password=user.password
    user_enquiry = Enquire(userId)
    '''
    user_enquiry.check_existence_of_user_in_the_register()==True
    user exists
    else 
    does not exists
    '''
    if(user_enquiry.check_existence_of_user_in_the_register()):
        
        return user_enquiry
    else:
        userEntry = AddUser(userId,password)
        userEntry.start_registering()
    return user_enquiry


def userLogin(user):
    userId = user.userId
    password = user.password
    login = Login(userId,password)
    login.compare_password()
    if(login.does_password_matches()):
        return login.get_jwt()
    else:
        return {
            "invalidLogin":True
            }


def sendJWTToken():
    pass

def convert_bytes_to_string(byte_data):
    return byte_data.decode('utf-8')


if __name__=='__main__':
    app.run(debug=True)