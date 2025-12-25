from models.user import User

class JobSeeker(User):
    role="job_seeker"
    def apply_job(self):
        return "Job Seeker can apply for jobs."