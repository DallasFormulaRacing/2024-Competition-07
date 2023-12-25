import pytest
from git_client import GitClient
from handler import Handler
import os


@pytest.fixture
def git_client():
    return GitClient(
        git_url=os.getenv("GITHUB_API_BASE")
    )


@pytest.fixture
def test_handler():
    return Handler(
        git_url=os.getenv("GITHUB_API_BASE")
    )
