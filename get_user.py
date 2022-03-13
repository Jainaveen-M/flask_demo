from main import Session,engine,User

local_session = Session(bind=engine)

user_list = local_session.query(User)

for user in user_list:
    print("ID -> {0} Username -> {1} email -> {2}".format(user.id,user.username,user.email))

