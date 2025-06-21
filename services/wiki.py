import requests

def search_wikipedia(query: str) -> str:
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "_")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No summary found.")
    else:
        return "No summary found for this topic."