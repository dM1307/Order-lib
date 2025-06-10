from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Enum, Integer, DateTime, func
from enum import Enum as PyEnum
import uuid

Base = declarative_base()


class JobStatus(PyEnum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Job(Base):

    __tablename__ = 'jobs'

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    client_id = Column(String(36), nullable=False)
    name = Column(String(255), nullable=False)
    schedule = Column(
        String,  # Changed from Base.String to String
        nullable=False  # cron or interval
    )
    status = Column(
        Enum(JobStatus),
        default=JobStatus.PENDING,
        nullable=False
    )
    retries = Column(Integer, default=0)
    priority = Column(Integer, default=5)
    created_at = Column(
        DateTime,  # Changed from Base.DateTime to DateTime
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime,  # Changed from Base.DateTime to DateTime
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "schedule": self.schedule,
            "status": self.status.value,  # status of the job
            "retries": self.retries,
            "created_at": self.created_at.isoformat(),  # creation timestamp
            "updated_at": self.updated_at.isoformat()  # update timestamp
        }
