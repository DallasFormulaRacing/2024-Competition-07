import json
import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DISCORD_URL = 'https://discord.com/api/webhooks/1190925331301937172/xmyN8IUsKCSVmtYN8JzGXzYu-V7W37GtAqFtamLMQWVya_2QEjmfshyhQJJ8lKd-flJc'

def lambda_handler(event, context):
    logger.info('Event:' + json.dumps(event))
    issues = event['issue']
    action = event['action']

    # Creating the message
    message = create_message(issues)

    # Sending the message
    if send_message(message):
        return {'statusCode': 200, 'body': json.dumps('Message sent to Discord')}
    else:
        return {'statusCode': 500, 'body': json.dumps('Failed to send message')}

def create_message(issue):
    message = f"New issue created in IC_Repo: {issue['title']}, 
      created by: {issue['user']['login']} - {issue['url']}"
    return message

def send_message(message) -> bool:
    try:
        response = requests.post(
            DISCORD_URL,
            json= {"content": message}
        )
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        print(err)
        return False