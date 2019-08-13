import requests
import json

if __name__ == '__main__':
    user_name = input('Enter your GitHub username: ')
    URL = "https://api.github.com/users/" + user_name + "/repos"

    response = requests.get(URL)
    repos = json.loads(response.text)

    repo_names = []
    for r in repos:
        repo_names.append(r['name'])

    for name in repo_names:
        print(name)
