from crypt import methods
import json
from flask import Flask,jsonify,request
from main import Session,engine,User

app = Flask(__name__)


@app.get('/')
def home():
    return "Home"

def get_users():
    local_session = Session()
    user_list = local_session.query(User)
    json_list = []
    for user in user_list:
        json_list.append({"id":user.id,"username":user.username,"email":user.email})
    return jsonify(json_list)

@app.get('/get-user')
def get_user():
   return get_users()
    #return "Getting users"
   # return {"id":1,"username":"jainaveen","email":'jainaveen@giotus.com'}


@app.route('/add-user',methods=['POST'])
def add_user():
    data = request.data
    return jsonify(data)
    

if __name__=='__main__':
    print("Main running....")
