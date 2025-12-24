class User:
    def __init__(self,username,email,role='Job Seeker'):
        self.username=username
        self.email=email
        self.role=role
        self._password=None

    def set_password(self,password):
        if len(password)<6:
            raise ValueError("Password must be at least 6 characters long.")
        self._password=password
    
    def check_password(self,password):
        return self._password==password
    
    def display_info(self):
        return f"Username: {self.username}, Email: {self.email}, Role:{self.role}"