from crypt import methods
from flask import Flask,jsonify,request
from main import Session,engine,User

app = Flask(__name__)


@app.get('/')
def home():
    return "Home"

def get_users():
    local_session = Session(bind=engine)
    user_list = local_session.query(User)
    json_list = []
    for user in user_list:
        json_list.append({"id":user.id,"username":user.username,"email":user.email})
    return jsonify(json_list)

@app.get('/get-user')
def get_user():
   return get_users()



@app.route('/add-user',methods=['POST'])
def add_user():
   data = request.json
   local_session = Session()
   new_user = User(id=data['id'],username=data['username'],email=data['email'])
   local_session.add(new_user)
   local_session.commit()
   return jsonify(data)
    

@app.route('/delete-user/<id>',methods=['DELETE'])
def delete_user(id):
    print(">>> Deleting user {0}".format(id))
    local_session = Session()
    user_id = local_session.query(User).filter(User.id==id).one()
    local_session.delete(user_id)
    local_session.commit()
    return "User deleted Successfully --> id : {0}".format(id)
    


@app.route('/update-user/<id>',methods=['PUT'])
def update_user(id):
    data = request.json
    local_session = Session()
    update_user = local_session.query(User).filter(User.id==id).one()
    update_user.username = data['username']
    local_session.commit()
    return "User Updated Successfully --> id : {0} name : {1}".format(id,data['username'])

if __name__=='__main__':
    print("Main running....")
