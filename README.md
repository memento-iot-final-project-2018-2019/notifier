# MEmento notifier
Python-based component sending a notification to the user's Twitter account when the door is opened, also play a sound alert that is stopped by reading a FOB or a card with a RFID rc522 module.

## Requirements
To have the necessary dependencies, create a virtual environment with
```
sudo apt-get install python3-dev python3-venv
python3 -m venv env
```


activate it
```
source env/bin/activate
```

Install `omxplayer-wrapper` package and its dependencies
```
sudo apt-get update && sudo apt-get install -y libdbus-1{,-dev}
```

```
pip install omxplayer-wrapper
```

and install the `python-twitter` package:
```
pip install python-twitter
```

Finally the`spidev` package and the `mrfc522` package:
```
pip install spidev
pip install mfrc522
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
