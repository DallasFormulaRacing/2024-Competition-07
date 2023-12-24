import os
import dotenv
import requests
from models.models import Issue

dotenv.load_dotenv()

GITHUB_API_BASE = "repos/DallasFormulaRacing/IC-Repo/issues"


class GitClient:

    def __init__(self, git_url: str):
        self.git_url = git_url

    def get_issues(self):
        url = f"https://api.github.com/{GITHUB_API_BASE}"
        issues = []

        while url:
            response = requests.get(url)
            if response.status_code == 200:
                issues.extend([Issue(**issue_data)
                              for issue_data in response.json()])

                if 'next' in response.links:
                    url = response.links['next']['url']
                else:
                    url = None
            else:
                response.raise_for_status()

        return issues

    def create_message(self, issue: Issue) -> str:
        pass
