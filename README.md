
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

1. Go to Telegram app and search '@BotFather' 

2. Click on /newbot

3. Give your bot a name and a username and your Done!

4. Add your api key in main.py on line 1

```bash
    python main.py
```
<br>

# For running this bot in a Server with Postgres

## Create Database in postgres
```
CREATE DATABASE telegram;

```

## Create Table for saving protected_list of users

```
CREATE TABLE protected_list ( id serial PRIMARY KEY, chat_id bigint, mobile text NOT NULL );

```

## Update password for user postgres 

```
ALTER USER myuser WITH ENCRYPTED PASSWORD 'postgres' PASSWORD 'md5';

```

<br>

