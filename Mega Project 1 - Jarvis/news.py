import os
import requests
from dotenv import load_dotenv

load_dotenv()


def getTopHeadlines():

    api_key = os.getenv("NEWS_API_KEY")

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    response = requests.get(url)

    if (response.status_code == 200):
        data = response.json()
        articles = data.get('articles', [])
        return articles

    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []
