import requests

def get_remotive_jobs(query):
    url = f"https://remotive.io/api/remote-jobs?search={query}"
    response = requests.get(url)
    jobs = response.json().get('jobs', [])
    return jobs

def get_github_jobs(query):
    url = f"https://jobs.github.com/positions.json?description={query}&location=remote"
    response = requests.get(url)
    jobs = response.json()
    return jobs
