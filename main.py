import requests
import pandas as pd
from dotenv import load_dotenv
from config import LEADSPICKER_API_KEY
from config import LEADSPICKER_CSRFTOKEN


def get_project_ids():
    """
    Fetches project IDs and names from the Leadspicker API.
    Sends a GET request to the Leadspicker projects endpoint using the provided API key and CSRF token.
    If the request is successful, parses the JSON response and extracts the 'id' and 'name' for each project.
    Returns a list of lists, where each inner list contains two dictionaries: one with the project 'id' and one with the project 'name'.
    Returns:
        list: A list of lists, each containing dictionaries with 'id' and 'name' of a project.
              Example: [[{'id': 123}, {'name': 'Project A'}], ...]
    Prints an error message if the API request fails.
    """
    request_url = "https://app.leadspicker.com/app/sb/api/projects"
    headers = {
        "accept": "application/json",
        "X-API-Key": LEADSPICKER_API_KEY,
        "X-CSRFToken": LEADSPICKER_CSRFTOKEN,
    }
    response = requests.get(request_url, headers=headers)

    if response.status_code == 200:
        project_data = response.json()
        
        project_ids = []
        for entry in project_data:
            project_ids.append([
                {"id": entry.get("id")},
                {"name": entry.get("name")}
            ])

    else:
        print(f"Failed to retrieve project IDs, with status code: {response.status_code}")

    return project_ids