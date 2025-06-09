from cp_lib.models.jobs import Job
from cp_lib.db import SessionLocal


# repositories/jobs_repository.py
class JobRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, job: Job):
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def get(self, job_id: str, client_id: str = None):
        q = self.db.query(Job)
        return q.filter(Job.id == job_id, Job.client_id == client_id).first()

    def list(self, client_id: str = None):
        q = self.db.query(Job)
        if client_id:
            q = q.filter(Job.client_id == client_id)
        return q.all()
