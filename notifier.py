import json
from TwitterAPI import *

def lambda_handler(event, context):
    with open("credentials.json", "r") as creds_file:
        creds = json.load(creds_file)
        oauth_consumer_key = creds["oauth_consumer_key"]
        oauth_consumer_secret = creds["oauth_consumer_secret"]
        oauth_token = creds["oauth_token"]
        oauth_token_secret = creds["oauth_token_secret"]
    
        api = TwitterAPI(consumer_key=oauth_consumer_key,
                        consumer_secret=oauth_consumer_secret,
                        access_token_key=oauth_token,
                        access_token_secret=oauth_token_secret)
        
        username = event.get('payload')
        msg = "Remember to LOCK the door!"
        
    
        event = {
        	"event": {
        		"type": "message_create",
        		"message_create": {
        			"target": {
        				"recipient_id": username
        			},
        			"message_data": {
        				"text": msg
        			}
        		}
        	}
        }

    
    send_msg = api.request('direct_messages/events/new', json.dumps(event))

    print('SUCCESS' if send_msg.status_code == 200 else 'PROBLEM: ' + send_msg.text)