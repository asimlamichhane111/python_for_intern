from models.admin import Admin
from models.employer import Employer
from models.job_seeker import JobSeeker
def main():
    admin=Admin("admin1",'admin@example.com')
    admin.set_password("admin123")
    employer=Employer("employer1",'employer@example.com')
    employer.set_password("emp12345")
    job_seeker=JobSeeker("job_seeker1",'job_seeker@example.com')
    job_seeker.set_password("seeker123")

    print(admin.display_info())
    print(admin.manage_users())

    print(employer.display_info())
    print(employer.post_job())

    print(job_seeker.display_info())
    print(job_seeker.apply_job())
    
if __name__=="__main__":
    main()