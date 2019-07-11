# MEmento notifier
Python-based component sending a notification to the user's Twitter account 

## Requirements
To have the necessary dependencies, create a virtual environment with and install the `TwitterAPI` package:


```
pip install TwitterAPI

```

You can check the dependencies and the documentation for the `TwitterAPI` library out at this link: https://github.com/geduldig/TwitterAPI .



Also remember to create a `credentials.json` file in the root folder of the repo, with this structure:

```
{
    "oauth_consumer_key": "<your twitter oauth consumer key>",
    "oauth_token": "<your twitter oauth token>",
    "oauth_token_secret": "<your twitter oauth token secret>",
    "oauth_consumer_secret": "<your twitter oauth consumer secret>"
}
```

The notifier is meant to be imported in an Amazon AWS Lambda function (check this link out for the AWS Lambda description, documentation and tutorial: https://aws.amazon.com/lambda/?nc1=f_ls).

If you want to activate the Lambda function using an IoT product, we suggest to use [Amazon AWS Iot Core](https://docs.aws.amazon.com/iot/index.html). AWS IoT Core is used to trigger a function on AWS Lambda.

The payload of the MQTT message sent to IoT Core has to be the user's Twitter account's ID (if you own a Twitter account, you can check your ID at this link: https://twitter.com/settings/your_twitter_data).

You can change the message to be sent by modifying the variable `msg` in the file `notifier.py`.

You can read more accurate details about how we developed our MEmento project at this link: <inserire link del blog>
    
N.B. In order to use this notifier, the user should own a Twitter account. 

# Authors
* Linkedin:
	* [Gabriele Cervelli](https://www.linkedin.com/in/<inserire user>/)
	* [Giovanni De Luca](https://www.linkedin.com/in/<inserire user>/)
	* [Antonino Di Maggio](https://www.linkedin.com/in/antonino-di-maggio-216479143/)
