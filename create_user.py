from main import Session,engine,User


local_session = Session(bind=engine)

new_user = User(id=10,username='demo user 2',email='demouser@giottus.com')
local_session.add(new_user)
local_session.commit()