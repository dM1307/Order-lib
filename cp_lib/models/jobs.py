from cp_lib.db import Base
from enum import Enum
import uuid


class JobStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Job(Base):

    __tablename__ = 'jobs'

    id = Base.Column(
        Base.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    clinet_id = Base.Column(Base.String(36), nullable=False)
    name = Base.Column(Base.String(255), nullable=False)
    schedule = Base.Column(
        Base.String,
        nullable=False  # cron or interval
    )
    status = Base.Column(
        Base.Enum(JobStatus),
        default=JobStatus.PENDING,
        nullable=False
    )
    retries = Base.Column(Base.Integer, default=0)
    priority = Base.Column(Base.Integer, default=5)
    created_at = Base.Column(
        Base.DateTime,
        server_default=Base.func.now(),
        nullable=False
    )
    updated_at = Base.Column(
        Base.DateTime,
        server_default=Base.func.now(),
        onupdate=Base.func.now(),
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
