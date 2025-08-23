from celery_app import app

@app.task
def test_scraper1():
    return "Hello from scraper1"