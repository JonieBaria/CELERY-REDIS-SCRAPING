# Celery Web Scraping Project

This project demonstrates how to use **Celery** with **Redis** (via Docker Compose) to run scraping tasks asynchronously in Python.  

It includes:
- A Celery app (`celery_app.py`)
- A scraping task (`job.py`)
- A script to submit tasks (`run_task.py`)
- A `docker-compose.yml` to run Redis and Redis Commander

---

## 🚀 Requirements

- Python 3.8+
- Docker & Docker Compose installed

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
celery
redis
requests
lxml
```

---

## ⚙️ Project Structure

```
CeleryProj/
│── celery_app.py       # Celery app configuration
│── job.py              # Scraping task
│── run_task.py         # Script to send tasks to Celery
│── requirements.txt
│── docker-compose.yml  # Redis & Redis Commander setup
```

---

## ▶️ Running the Project

### 1. Start Redis & Redis Commander with Docker Compose
```bash
docker-compose up -d
```

This starts:
- **Redis** at `localhost:6379`
- **Redis Commander** (web UI) at [http://localhost:8084](http://localhost:8084)

---

### 2. Start the Celery Worker
Run the worker so it can process tasks:

```bash
celery -A celery_app worker -l info --pool=solo
```

> ⚠️ On Windows, `--pool=solo` is required to avoid multiprocessing issues.

If successful, you should see:
```
[tasks]
  . job.process
```

---

### 3. Submit a Task
Run the task script:

```bash
python run_task.py
```

Output:
```
Task submitted!
Result: {'url': 'https://example.com', 'title': 'Example Domain'}
```

---

## 📦 Example Task

Defined in `job.py`:

```python
@app.task
def process(url):
    response = requests.get(url, timeout=10)
    tree = html.fromstring(response.content)
    title = tree.xpath("//title/text()")
    return {"url": url, "title": title[0] if title else "No title found"}
```

---

## 🛠️ Extending

To add more scraping tasks:
1. Create a new file (e.g., `tasks/google.py`)
2. Import `app` from `celery_app.py`
3. Define your `@app.task` functions
4. Ensure the module is imported (or use `app.autodiscover_tasks()`)

Example:
```python
from celery_app import app

@app.task
def scrape_google(query):
    # Your scraping logic
    return {"query": query, "result": "..."}
```

---

## ✅ Notes

- Redis is managed entirely via Docker Compose (no need to install it manually).
- Use `result.get(timeout=20)` in `run_task.py` to wait for results.
- For concurrent workers, run this on **Linux/WSL** (so you can use the default `prefork` pool).

---

## 📚 References
- [Celery Documentation](https://docs.celeryq.dev/en/stable/)
- [Redis Documentation](https://redis.io/docs/)
- [Redis Commander](https://hub.docker.com/r/rediscommander/redis-commander)
