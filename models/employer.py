from models.user import User

class Employer(User):
    def post_job(self):
        return "Employer can post a job."