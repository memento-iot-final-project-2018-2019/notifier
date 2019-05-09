# MEmento notifier
Python-based component sending a notification to the user's Twitter account when the door is opened

## Requirements
To have the necessary dependencies, create a virtual environment, activate it and install the `python-twitter` package: 
```
pip install python-twitter
```

Also remember to create a `credentials.json` file in the root folder of the repo, with this structure:
```
{
    "oauth_consumer_key": "<your twitter oauth consumer key>",
    "oauth_token": "<your twitter oauth token>",
    "oauth_token_secret": "<your twitter oauth token secret>",
    "oauth_consumer_secret": "<your twitter oauth consumer secret>"
}
```