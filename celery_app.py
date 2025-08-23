from celery import Celery
import pkgutil
import importlib

app = Celery(
    "scraper",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
    # include=["scraper.scraper1"]
)

# import scraper

package = "scraper"
for _, module_name, _ in pkgutil.iter_modules([package]):
    importlib.import_module(f"{package}.{module_name}")
    backend="redis://localhost:6379/1"


# Import tasks explicitly so Celery knows about them
import scraper.job

# Optional settings
# app.conf.update(
#     task_serializer="json",
#     result_serializer="json",
#     accept_content=["json"],
#     timezone="Asia/Manila",
#     enable_utc=True,
# )
