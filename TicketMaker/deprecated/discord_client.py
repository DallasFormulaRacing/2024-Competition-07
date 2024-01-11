import discord
import requests


class DiscordClient(discord.Client):
    def __init__(self, channel_id: int):
        super().__init__()
        self.channel_id = channel_id

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_github_issue(self, issue_info):
        channel = self.get_channel(self.channel_id)
        message = f"New issue created: {issue_info['title']} - {issue_info['url']}"
        await channel.send(message)
