from main import Session,engine,User


local_session = Session(bind=engine)

update_user = local_session.query(User)
for i in update_user:
    print(i.id)
    if i.id==3:
        i.username = 'updated'
        break
local_session.commit()
print(update_user)
