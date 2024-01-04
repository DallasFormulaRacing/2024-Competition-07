import pytest
from git_client import GitClient
from handler import Handler
from discord_client import DiscordClient
import os


@pytest.fixture
def git_client():
    return GitClient(
        git_url=os.getenv("GITHUB_API_BASE")
    )


@pytest.fixture
def test_handler():
    return Handler(
        git_url=os.getenv("GITHUB_API_BASE"),
        discord_channel_id=1187644034852847670
    )


@pytest.fixture
def test_disc():
    return DiscordClient(
        channel_id=1187644034852847670
    )
