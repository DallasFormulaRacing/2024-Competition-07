from git_client import GitClient
from models.models import Message
from typing import List


class Handler:
    def __init__(self, git_url: str):
        self.git_client = GitClient(git_url)

    def get_issues(self) -> List[Message]:
        issues = self.git_client.get_issues()
        return issues

    def make_message(self, issues: List) -> List[Message]:
        messages = []

        for issue in issues:
            label_dicts = [label.dict()
                           for label in issue.labels] if issue.labels else []

            message = Message(
                title=issue.title,
                body=issue.body,
                labels=label_dicts,
                created_by=issue.user.login,
                created_at=issue.created_at,
            )
            messages.append(message)

        return messages
