import requests
import json

USERNAME = "AK101395"

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url)

if response.status_code == 200:

    repos = response.json()

    projects = []

    for repo in repos:

        projects.append({
            "name": repo["name"],
            "description": repo["description"],
            "url": repo["html_url"]
        })

    with open(
        "projects.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            projects,
            file,
            indent=4
        )

    print("Projects Updated")

else:

    print("GitHub API Error")