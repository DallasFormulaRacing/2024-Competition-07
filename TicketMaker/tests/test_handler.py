import asyncio


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


def test_send_messages(test_handler):
    issues = test_handler.get_issues()
    messages = test_handler.make_message(issues)
    test_handler.send_messages(messages)


def test_disc_client(test_disc, test_handler):
    issues = test_handler.get_issues()
    message = asyncio.run(test_disc.on_github_issue(issue_info=issues[0]))
    expected_message = f"New issue created: {issues[0]['title']} - {issues[0]['url']}"
    assert message == expected_message
