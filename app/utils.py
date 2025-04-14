import re

def extract_user_input(user_input):
    # A basic example to extract job title, skills, and location (improve this as needed)
    job_title = ''
    skills = []
    location = ''
    
    # Extracting skills (just a basic example)
    skills = re.findall(r'\b(?:python|java|javascript|sql|react|html|css)\b', user_input.lower())
    
    # Assuming job title is the first word and location as the last word
    words = user_input.split()
    if words:
        job_title = words[0]
        location = words[-1]
    
    return job_title, skills, location
