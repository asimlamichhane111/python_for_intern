class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
        self._password=None

    def set_password(self,password):
        if len(password)<6:
            raise ValueError("Password must be at least 6 characters long.")
        self._password=password
    
    def check_password(self,password):
        return self._password==password
    
    def get_role(self):
        return self.__class__.__name__
    
    def display_info(self):
        return f"{self.get_role()} | {self.username} | {self.email}"