import requests
import json

URL = "https://api.github.com/users/octocat/repos"

def fetch_data():
    response = requests.get(URL)
    return response.json()

def process_data(data):
    final = []
    for repo in data[:5]:
        final.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "language": repo["language"],
            "url": repo["html_url"]
        })
    return final

def save_json(data, filename="output.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    raw = fetch_data()
    processed = process_data(raw)

    print("\n Top 5 Public Repositories:\n")
    for r in processed:
        print(r)

    save_json(processed)
    print("\n Output saved to output.json\n")
