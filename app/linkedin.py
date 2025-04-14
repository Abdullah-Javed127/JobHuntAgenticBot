import requests

def get_linkedin_posts(company_username):
    url = f"https://linkedin-api8.p.rapidapi.com/get-company-posts?username={company_username}&start=0"
    headers = {
        'x-rapidapi-host': 'linkedin-api8.p.rapidapi.com',
        'x-rapidapi-key': '58ab299e40msh80d53e9fcac874fp11f339jsnbc1e813bea34'
    }
    response = requests.get(url, headers=headers)
    posts = response.json().get('data', [])
    return posts
