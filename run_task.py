from scraper.job import process
<<<<<<< HEAD
#
=======

>>>>>>> f238942f5a58cdf7fc5d922a3c6efb42f7577879
if __name__ == "__main__":
    url = "https://example.com"
    result = process.delay(url)   # send task to Celery worker
    print("Task submitted!")

    # You can block until result is ready:
    print("Result:", result.get(timeout=60))
    print("test")
