import json
import os
from models.admin import Admin
from models.employer import Employer
from models.job_seeker import JobSeeker
from config import DATA_DIR

USER_FILE=os.path.join(DATA_DIR,"users.json")
# print(USER_FILE)

def load_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE,"r") as f:
        data=json.load(f)
    
    users=[]
    for item in data:
        role=item['role']
        username=item['username']
        email=item['email']

        password=item['password']
        if role=="admin":

            user=Admin(username,email)
        elif role=="employer":
            user=Employer(username,email)
        elif role=="job_seeker":
            user=JobSeeker(username,email)
        else:
            continue
        user.set_password(password)
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