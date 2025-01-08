class User:
    def __init__(self, name, email, password, job, company):
        self.name = name
        self.email = email
        self.password = password
        self.job = job
        self.company = company
        
    def change_password(self, new_password):
        self.password = new_password
    
    def update_email(self, new_email):
        self.email = new_email
    
    def change_job(self, new_job):
        self.job = new_job
        
    def get_user_info(self):
        print(f"Name: {self.name} \nEmail: {self.email} \nJob: {self.job} \nCompany: {self.company}")
        
