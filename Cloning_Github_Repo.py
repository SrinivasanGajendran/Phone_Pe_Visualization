import requests
import json
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git

def check():
    path = "D:/python/project/PhonePe_data"
    isExist = os.path.exists(path)
    if isExist:
        pass
    else:
        url = "https://api.github.com/repos/PhonePe/pulse"
        response = requests.get(url)
        if response.status_code == 200:
            repo = json.loads(response.text)
            clone_url = repo["clone_url"]
            repo_url = clone_url
            local_path = "D:/python/project/PhonePe_data"
            repo_1 = git.Repo.clone_from(repo_url, local_path)


