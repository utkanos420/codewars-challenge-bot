# Codewars challenge bot

<i>notice that this bot is still not created</i>
<i>repository is opened for everyone as a reference etc, and can be used by everyone</i>

## What's this?

I wanna try creating a telegram bot making codewars challenges between 2 or more tg users, like a battle who'll faster solved a kata etc

This bot will use codewars api data to handle changes on user's profile, like a kata was solved, and after it redict it to tg



## What technologies are used?

> Aiogram3 for bot's logic<br>
> SQLalchemy + aio/sqlite3 for DBs<br>
> Alembic for DBs versioning<br>
> Requests for connecting to open codewars api<br>
> Jinja2 for preparing bot's messages (structured samples in 1 folder instead of writing bot's answers in bot's logic)<br>
> Pydantic, pydantic-settings validations<br>
> <i>Poetry for package manage</i><br>

## Is it already done?

Currently, on this commit, bot obviously do nothing. It can create user's profile and save in DB, validate user through a form of creating a challenge (without creating it as a challenge in DB etc)

## Can I use this repository?

For sure, you can use it, the project is open-source and can be used by everyone.

## How do I start bot?

> Clone the repository
> Generate a botfather telegram bot token and paste it in .env file
> Create a Python virtual environment >3.13<br>
> Install all dependencies: pip install -r requirements.txt in python venv<br>
> cd bot<br>
> python main.py<br>
