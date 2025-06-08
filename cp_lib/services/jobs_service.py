import uuid
from cp_lib.models.job import Job
from cp_lib.repositories.job_repository import JobRepository


class JobService:
    def __init__(self):
        self.repo = JobRepository()

    def create_job(
      self, name: str,
      schedule: str,
      retries: int = 0,
      priority: int = 0
      ):
        job = Job(
            id=str(uuid.uuid4()),
            name=name,
            schedule=schedule,
            retries=retries,
            priority=priority
        )
        return self.repo.create(job)

    def get_job(self, job_id: str):
        return self.repo.get(job_id)

    def list_jobs(self):
        return self.repo.list()
