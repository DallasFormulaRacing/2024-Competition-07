def test_git_client_init(git_client):
    issues = git_client.get_issues()
    assert len(issues) > 20
