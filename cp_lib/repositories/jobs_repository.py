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

    def get(self, job_id: str):
        return self.db.query(Job).filter(Job.id == job_id).first()

    def list(self):
        return self.db.query(Job).all()
