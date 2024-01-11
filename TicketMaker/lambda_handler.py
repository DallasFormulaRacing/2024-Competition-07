import json
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1194890547706462208/XnMJT2L40HbZr8L7qHTije4Un3XvTW8kwZElLa7nndhldBEPrteVJtveNTXt5p6Ox4eS"


def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event))

    if 'body' in event:
        payload = json.loads(event['body'])

        if 'issue' in payload and payload.get('action') == 'opened':
            issue = payload['issue']
            action = payload['action']

            message = create_message(issue, action)
            response = send_message_to_discord(message)

            logger.info("Discord response: " + json.dumps(response))

            return {
                'statusCode': 200,
                'body': json.dumps('Message sent to Discord')
            }
        else:
            logger.info("Ignored action: " +
                        payload.get('action', 'No action'))
            return {
                'statusCode': 200,
                'body': json.dumps('Ignored non-open issue action')
            }
    else:
        logger.error("No body key in event")
        return {
            'statusCode': 400,
            'body': json.dumps('No body in the received event')
        }


def create_message(issue, action):
    title = issue.get('title', 'No title')
    user_login = issue['user']['login']
    issue_number = issue['number']
    issue_url = issue['html_url']

    message = f"Issue #{issue_number}, titled: {title} was created by {user_login}. You can view it at {issue_url}"
    return message


def send_message_to_discord(message):
    headers = {'Content-Type': 'application/json'}
    payload = {'content': message}

    try:
        response = requests.post(
            DISCORD_WEBHOOK_URL, json=payload, headers=headers)
        response.raise_for_status()
        return {'status': 'success', 'response': response.text}
    except requests.exceptions.RequestException as error:
        logger.error(f"Error sending message to Discord: {error}")
        return {'status': 'failure', 'error': str(error)}
