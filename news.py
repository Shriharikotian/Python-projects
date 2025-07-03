import requests # pip install requests

query = input("What type of news are you interested in today? ")
api = "7c7eaf7d099b4d5986f1aaaa4af59fdd"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-03&sortBy=publishedAt&apiKey={api}"

print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
