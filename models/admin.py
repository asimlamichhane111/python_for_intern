from models.user import User

class Admin(User):
    role="admin"
    def manage_users(self):
        return "Admin can manage all users."