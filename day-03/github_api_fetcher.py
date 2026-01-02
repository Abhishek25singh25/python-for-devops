import requests
import json

URL = "https://api.github.com/users/octocat/repos"


def fetch_data():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error: Failed to fetch data from GitHub API")
        return []


def process_data(data):
    final = []

    for repo in data[:5]:
        final.append({
            "name": repo.get("name"),
            "stars": repo.get("stargazers_count"),
            "language": repo.get("language"),
            "url": repo.get("html_url")
        })

    return final


def save_json(data, filename="output.json"):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Output saved to output.json")
    except IOError:
        print("Error: Could not write to file")


if __name__ == "__main__":
    raw = fetch_data()

    if not raw:
        print("No data received")
    else:
        processed = process_data(raw)

        print("\nTop 5 Public Repositories:\n")
        for r in processed:
            print(r)

        save_json(processed)
