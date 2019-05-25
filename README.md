# MEmento Notifier
Python-based component sending a notification to the user's phone running Google services with GAssist, when the door is opened (VCNL4040 proximity sensor), also play a sound alert that is stopped by reading a FOB or a card with a RFID RC522 module.

## Requirements
- A Google developer account with `Actions API` and `Assistant API` enabled from Google Cloud Platform.
- An `Actions project` created according to [this page](https://developers.google.com/assistant/sdk/guides/library/python/embed/config-dev-project-and-account)

To have the necessary dependencies, create a virtual environment with
```
sudo apt-get install python3-dev python3-venv
python3 -m venv env
env/bin/python -m pip install --upgrade pip setuptools wheel
```


activate it
```
source env/bin/activate
```

Install `omxplayer-wrapper` package and its dependencies for **sound alert**
```
sudo apt-get update && sudo apt-get install -y libdbus-1{,-dev}
```

```
pip install omxplayer-wrapper
```

Install the`spidev` and the `mrfc522` packages for our **RFID sensor**:
```
pip install spidev
pip install mfrc522
```
Clone in your `/home/pi` directory this [repo](https://github.com/adafruitAdafruit_CircuitPython_VCNL4040.git) for our **proximity sensor** and run:
```
cd adafruitAdafruit_CircuitPython_VCNL4040
python setup.py install
cd ..
```

 [configure your Google Developer account](developers.google.com/assistant/sdk/guides/library/python/embed/config-dev-project-and-account) with which you created your Actions project, then [register the device model](https://developers.google.com/assistant/sdk/guides/library/python/embed/register-device) **WITH** `OnOff` **AS A TRAIT**

Now run
```
sudo apt-get install portaudio19-dev libffi-dev libssl-dev libmpg123-dev
python -m pip install --upgrade google-assistant-library==1.0.1
python -m pip install --upgrade google-assistant-sdk[samples]==0.5.1
python -m pip install --upgrade google-auth-oauthlib[tool]
```
You need to generate credentials with the JSON downloaded during device registration
```
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --scope https://www.googleapis.com/auth/gcm \
      --save --headless --client-secrets /path/to/client_secret_client-id.json
```

Copy the returned URL and paste it into a browser (this can be done on any machine). The page will ask you to sign in to your Google account. Sign into the Google account that created the developer project.

After you approve the permission request from the API, a code will appear in your browser, such as "4/XXXX". Copy and paste this code into the terminal.

Now you can run a test:
```
googlesamples-assistant-hotword --project-id my-dev-project --device-model-id my-model --query 'hello'
```
In order to run the repo script, from your `/home/pi` directory:
```
cd notifier
python hotword.py --project-id my-dev-project --device-model-id my-model --query 'hi, turn on'
```
