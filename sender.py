import twitter
import json

with open("credentials.json", "r") as creds_file:
    creds = json.load(creds_file)
    oauth_consumer_key = creds["oauth_consumer_key"]
    oauth_token = creds["oauth_token"]
    oauth_token_secret = creds["oauth_token_secret"]
    oauth_consumer_secret = creds["oauth_consumer_secret"]

    api = twitter.Api(consumer_key=oauth_consumer_key,
                    consumer_secret=oauth_consumer_secret,
                    access_token_key=oauth_token,
                    access_token_secret=oauth_token_secret)

    msg = input("Type the message to send: ")
    username = input("Type the twitter handle of the user to send the message to: ")
    send_msg = api.PostDirectMessage(msg, user_id=None, screen_name=username)