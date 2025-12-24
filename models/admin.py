from models.user import User

class Admin(User):
    def manage_users(self):
        return "Admin can manage all users."