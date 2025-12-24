import json
import os
from models.admin import Admin
from models.employer import Employer
from models.job_seeker import JobSeeker
from config import DATA_DIR

USER_FILE=os.path.join(DATA_DIR,"users.json")

def load_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE,"r") as f:
        data=json.load(f)
    
    users=[]
    for item in data:
        role=item['role']
        if role=="admin":
            user=Admin(item['username'],item['email'])
        elif role=="employer":
            user=Employer(item['username'],item['email'])
        elif role=="job_seeker":
            user=JobSeeker(item['username'],item['email'])
        else:
            continue
        user.set_password(item["password"])
        users.append(user)
    return users

def save_users(users):
    data=[]
    for user in users:
        data.append({
            "username":user.username,
            "email":user.email,
            "password":user._password,
            "role":user.get_role()
        })
    with open(USER_FILE,"w") as f:
        json.dump(data,f)