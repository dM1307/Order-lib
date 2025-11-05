# 📦 Order-lib

Order-lib is a **Python library** that provides SQLAlchemy models and utilities for managing **Jobs, Job Dependencies, and Job Runs**.
It is designed as the **business logic layer** that can be plugged into APIs or orchestrators for task scheduling and execution tracking.

---

## ✨ Features

* 💄 **ORM Models with SQLAlchemy**

  * `Job` → defines a unit of work.
  * `JobDependency` → defines dependencies between jobs.
  * `JobRun` → tracks executions of jobs.

* 🔄 **Alembic-ready** for schema migrations.

* ⚡ **Reusable**: Works as a plug-and-play library in your API or orchestration systems.

* 🧙‍♂️ **Hexagonal Architecture friendly**: Keeps business logic decoupled from interface layers.

---

## 📊 Entity Relationship Diagram

```mermaid
erDiagram
    Job {
        int id PK
        string name
        string description
    }
    JobDependency {
        int id PK
        int job_id FK
        int depends_on_id FK
    }
    JobRun {
        int id PK
        int job_id FK
        string status
        datetime started_at
        datetime finished_at
    }

    Job ||--o{ JobDependency : "depends on"
    Job ||--o{ JobRun : "has runs"
```

---

## 🔄 Job Execution Flow

Here’s how a job flows through dependencies into execution:

```mermaid
graph TD
    A[📝 Define Job] --> B[🔗 Add Dependencies]
    B --> C[✅ Dependency Check Passed?]
    C -- Yes --> D[🚀 Start JobRun]
    C -- No --> E[⏳ Wait for Dependencies]
    D --> F[📊 Track Status]
    F --> G[🗂️ Store in Database]
```

---

## 📥 Installation

Clone and install locally:

```bash
git clone https://github.com/dM1307/Order-lib.git
cd Order-lib
pip install .
```

Or install in **editable/development mode**:

```bash
pip install -e .
```

---

## ⚙️ Setup

1. **Configure your database**
   Add your connection string in `.env`:

   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/mydb
   ```

2. **Run migrations**
   Alembic is already included, so you can migrate schemas easily:

   ```bash
   alembic upgrade head
   ```

---

## 🚀 Usage Example

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from order_lib.models import Job, JobDependency, JobRun, Base

engine = create_engine("postgresql://user:password@localhost:5432/mydb")
Session = sessionmaker(bind=engine)
session = Session()

# Create tables (only first-time setup)
Base.metadata.create_all(engine)

# Create jobs
job_a = Job(name="generate_report")
job_b = Job(name="send_email")
session.add_all([job_a, job_b])
session.commit()

# Add dependency (job_b depends on job_a)
dependency = JobDependency(job_id=job_b.id, depends_on_id=job_a.id)
session.add(dependency)
session.commit()

# Record a job run
run = JobRun(job_id=job_a.id, status="started")
session.add(run)
session.commit()
```

---

## 🔧 Migrations (Alembic)

1. Generate a migration:

   ```bash
   alembic revision --autogenerate -m "Add priority to Job"
   ```

2. Apply it:

   ```bash
   alembic upgrade head
   ```

3. Rollback if needed:

   ```bash
   alembic downgrade -1
   ```

---

## 🧑‍💻 Development

* Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

* Run migrations for dev DB:

  ```bash
  alembic upgrade head
  ```

* Code style: Follows `PEP8` (configured via `setup.cfg`).


---

### 💡 Next Steps

* [ ] Add unit tests 🧪
* [ ] Publish package to PyPI 📦
* [ ] Add CI/CD workflow ✅
* [ ] Document advanced queries & filters 🔍

---
