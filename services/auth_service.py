from storage.user_storage import load_users, save_users
from models.admin import Admin
from models.employer import Employer
from models.job_seeker import JobSeeker

def register_user(username,email,password,role):
    users=load_users()

    for user in users:
        if user.username==username:
            raise ValueError("Username already exists")
        
    if role=="admin":
        user=Admin(username,email)
    elif role=="employer":
        user=Employer(username,email)
    else:
        user=JobSeeker(username,email)

    user.set_password(password)
    users.append(user)
    save_users(users)
    return user

def authenticate_user(username,password):
    users=load_users()
    for user in users:
        if user.username==username and user.check_password(password):
            return user
    return None
