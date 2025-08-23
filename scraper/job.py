from time import sleep
import requests
from lxml import html
from celery_app import app  # Import the Celery app instance


@app.task
def process(url="https://example.com"):
    try:
        # Fetch the page
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse the HTML
        tree = html.fromstring(response.content)

        # Extract the <title> text
        title = tree.xpath("//title/text()")
        title_text = title[0].strip() if title else "No title found"

        print(f"Fetched title: {title_text}")
        return {"url": url, "title": title_text}

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return {"url": url, "error": str(e)}
