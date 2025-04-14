from flask import Blueprint, request, jsonify
from .job_search import get_remotive_jobs, get_github_jobs
from .linkedin import get_linkedin_posts
from .utils import extract_user_input

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/find_jobs_and_posts', methods=['POST'])
def find_jobs_and_posts():
    user_input = request.json.get('user_input')
    job_title, skills, location = extract_user_input(user_input)

    # Fetch job listings from Remotive and GitHub
    remotive_jobs = get_remotive_jobs(' '.join(skills))
    github_jobs = get_github_jobs(' '.join(skills))

    # Fetch LinkedIn posts for a specific company (e.g., Google)
    linkedin_posts = get_linkedin_posts('google')

    # Combine results and return as JSON
    results = {
        "jobs": remotive_jobs + github_jobs,
        "linkedin_posts": linkedin_posts
    }

    return jsonify(results)
