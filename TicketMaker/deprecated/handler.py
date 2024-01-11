from deprecated.git_client import GitClient
from models.models import Message, Issue
from deprecated.discord_client import DiscordClient
from typing import List
import os


class Handler:
    def __init__(self, git_url: str, discord_channel_id: int):
        self.git_client = GitClient(git_url)
        self.discord_client = DiscordClient(discord_channel_id)

    def get_issues(self) -> List[Issue]:
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

    def send_messages(self, messages: List[Message]):
        self.discord_client.on_ready()
        self.discord_client.run(os.getenv("DISCORD_TOKEN"))

        for message in messages:
            self.discord_client.on_github_issue(message)
