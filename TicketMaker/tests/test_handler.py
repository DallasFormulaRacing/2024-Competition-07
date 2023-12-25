def test_git_client_init(git_client):
    issues = git_client.get_issues()
    assert len(issues) > 20


def test_get_issues(test_handler):
    messages = test_handler.get_issues()
    assert len(messages) == 38


def test_make_message(test_handler):
    issues = test_handler.get_issues()
    messages = test_handler.make_message(issues)
    assert len(messages) == 38
