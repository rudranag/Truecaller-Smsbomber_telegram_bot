
# Truecaller and Smsbomber telegram bot

This bot can provide you Truecaller and Smsbomber features using api requests

Made using [python_telegram_bot](https://github.com/python-telegram-bot/python-telegram-bot)





## Requirements


You can Install requirements using
```sh
pip install -r requirements.txt
```


 

## Usage

To get you bot Api Key

Go to Telegram app and search '@BotFather' 

Click on /newbot

Give your bot a name and a username and your Done!

Add your api_key to environment variable and add it to line 12.
or replace the line with api_key = actual api key



#### Procfile (Normal version)

The Procfile for Normal version of the bot should be.

```bash
    worker: python main.py
```

