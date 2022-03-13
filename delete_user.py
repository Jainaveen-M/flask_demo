import imp
from multiprocessing.spawn import import_main_path

from numpy import delete
from main import Session,engine,User
from sqlalchemy import delete

local_session = Session()
local_session.query(User).filter(User.email=='jainaveen@giottus.com').delete()

#local_session.delete(delete_user)
local_session.commit()
