"""
Task 4 - GitHub REST API snippet.

This example fetches public repositories for a given GitHub user
and prints the repository names as JSON.
"""

import json
import requests


def get_github_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(
        url,
        params={"per_page": 100},
        timeout=10,
    )

    response.raise_for_status()

    repositories = response.json()

    return [
        repository["name"]
        for repository in repositories
    ]


if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()

    try:
        names = get_github_repositories(username)
        print(json.dumps(names, indent=2))
    except requests.RequestException as exc:
        print(json.dumps({"error": str(exc)}, indent=2))
