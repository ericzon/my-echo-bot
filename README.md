Echo-bot
========

My aim with this project is just to give a simple base to help tackling the real problem. It's based in the example from Microsoft bot framework.

## Setup

In this case I'm using python 3.12.3. I suggest to use poetry or similar but is up to you. Main dependencies are reflected in pyproject.toml.

Once you've installed all the dependencies, you can start the application with:
```
poetry run python .\main.py
```

## Env variables

```
PORT=3000

# Bot: Fill these values from Azure Bot settings
BOT_ID=
BOT_PASSWORD=
BOT_SECRET=

# Fill these values from Azure Speech service settings
SPEECH_SVC_KEY=
SPEECH_REGION=
SPEECH_ENDPOINT=

```

## Public folder

Once you have started the application, it will expose the chatbot client in http://localhost:<PORT>/ or http://localhost:<PORT>/index_speech.html

It includes 2 versions of client, the basic one and another version using Azure Speech for STT (Speech to text).
