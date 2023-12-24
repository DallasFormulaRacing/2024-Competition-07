import pytest
from git_client import GitClient
import os


@pytest.fixture
def git_client():
    return GitClient(

        git_url=os.getenv("GITHUB_API_BASE")
    )
