from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
import sqlalchemy
from datetime import datetime
import pymysql
import pandas as pd


Base = declarative_base()

# engine = create_engine('mysql+pymysql://root:root@123@3306/demo')
# df = pd.read_sql('SELECT * FROM user', engine)


username = 'root'
password = 'root@123'
host = 'localhost'
port = 3306

engine = create_engine("mysql+pymysql://root:root12345@localhost:3306/demo",echo=True)
with engine.connect() as conn:
   # Do not substitute user-supplied database names here.
    conn.execute("CREATE DATABASE IF NOT EXISTS demo")

class User(Base):
    __tablename__='user'
    id=Column(Integer(),primary_key=True)
    username=Column(String(30),nullable=True)
    email=Column(String(30),nullable=True)
    date_created=Column(DateTime(),default=datetime.utcnow)

    def __repr__(self):
        #return f"User>> {self.id} {self.username}"
        return "User>>{0}{1}".format(self.username,self.email)




Session = sessionmaker(bind=engine)
session = Session()
print("+++++++ Before addinf new user +++++")
# for instance in session.query(User):
#     //print(f'{instance.username} {instance.email}')


# new_user = User(id=1,username='d',email='jainaveen@giottus.com')
# session.add(new_user)
# session.commit()
print("++++++ After adding new user +++++++")
# for instance in session.query(User):
#     print(f'{instance.username} {instance.email}')

# print(new_user)

