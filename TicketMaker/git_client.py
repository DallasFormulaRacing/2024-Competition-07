import os
import dotenv
import requests
from models.models import Issue, Message
from typing import List

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

    def create_message(self, issues: List) -> Message:

        for issue in issues:
            message = Message(
                title=issue["title"],
                body=issue["body"],
                labels=issue["labels"]["name"],
                created_by=issue["user"]["login"],
                created_at=issue["created_at"],
            )
            return message
