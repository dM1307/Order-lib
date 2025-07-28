from pydantic import BaseModel


class JobCreate(BaseModel):
    name: str
    clinet_id: str
    schedule: str
    retries: int = 0
    priority: int = 5


class JobRead(JobCreate):
    id: str
    status: str
