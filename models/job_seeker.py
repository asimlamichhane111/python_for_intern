from models.user import User

class JobSeeker(User):
    def apply_job(self):
        return "Job Seeker can apply for jobs."