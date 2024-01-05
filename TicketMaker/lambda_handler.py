import json
import requests

DISCORD_URL = 'https://discord.com/api/webhooks/1190925331301937172/xmyN8IUsKCSVmtYN8JzGXzYu-V7W37GtAqFtamLMQWVya_2QEjmfshyhQJJ8lKd-flJc'

def lambda_handler(event, context):
    issues = event['issue']
    action = event['action']

    # Creating the message
    message = create_message(issues)

    # Sending the message
    send_message(message)

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to Discord')
    }

def create_message(issue):
    message = f"New issue created in IC_Repo: {issue['title']}, 
      created by: {issue['user']['login']} - {issue['url']}"
    return message

def send_message(message) -> bool:
    try:
        response = requests.post(
            DISCORD_URL,
            data= {"content": message},
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        print(err)
        return False