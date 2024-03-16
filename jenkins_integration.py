import requests
import os

def create_pipeline():
    # Jenkins API endpoint for creating a pipeline
    jenkins_url = os.environ.get("http://34.229.88.104")
    jenkins_username = os.environ.get("admin123")
    jenkins_password = os.environ.get("Arun12092001")

    if not jenkins_url:
        print("Jenkins URL not provided.")
        return False

    # Example pipeline configuration
    pipeline_config = {
        "name": "My Pipeline",
        "stages": [
            {"name": "Stage 1", "steps": ["echo 'Hello World'"]},
            {"name": "Stage 2", "steps": ["echo 'Goodbye World'"]}
        ]
    }

    # Make HTTP request to create pipeline
    try:
        response = requests.post(jenkins_url, auth=(jenkins_username, jenkins_password), json=pipeline_config)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print("Error creating Jenkins pipeline:", e)
        return False

