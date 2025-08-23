from scraper.job import process
#
if __name__ == "__main__":
    url = "https://example.com"
    result = process.delay(url)   # send task to Celery worker
    print("Task submitted!")

    # You can block until result is ready:
    print("Result:", result.get(timeout=60))
    print("test")
