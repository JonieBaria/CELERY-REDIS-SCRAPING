from celery import Celery

app = Celery(
    "job",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1"
)

# Import tasks explicitly so Celery knows about them
import job

# Optional settings
# app.conf.update(
#     task_serializer="json",
#     result_serializer="json",
#     accept_content=["json"],
#     timezone="Asia/Manila",
#     enable_utc=True,
# )
