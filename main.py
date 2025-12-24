from models.admin import Admin
# from models.employer import Employer
# from models.job_seeker import JobSeeker
from storage.user_storage import load_users, save_users
def main():

    users=load_users()

    if not users:
        admin=Admin("admin1",'admin@example.com')
        admin.set_password("admin123")
        users.append(admin)
        save_users(users)
        print("Initial user created.")

    for user in users:
        print(user.display_info())

if __name__=="__main__":
    main()