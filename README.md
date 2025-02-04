# Echo-bot

My aim with this project is just to give a simple base to help tackling the real problem. It's based in the example from Microsoft bot framework.

## Prerequisites

1. Have a computer
2. Install python, note that tensorflow latest version is not compatible if python is higher than 3.11
3. Install poetry
4. Install project dependencies using poetry with

```
poetry install
```

5. create a .env file in the root project with the content in the section env variables below

## Setup

In this case I'm using python 3.12.3. I suggest to use poetry or similar but is up to you. Main dependencies are reflected in pyproject.toml.

Once you've installed all the dependencies, you can start the application with:

```
poetry run python main.py
```

## Env variables

```
PORT=3000
DOMAIN=http://localhost

# Bot: Fill these values from Azure Bot settings
BOT_ID=
BOT_PASSWORD=
BOT_SECRET=

# Fill these values from Azure Speech service settings
SPEECH_SVC_KEY=
SPEECH_REGION=
SPEECH_ENDPOINT=

```

## Front end

The front end code is placed in folder client.
To install the dependencies go to the folder `client` and execute `npm install`

Once the backend is started the frontend is started, as well, but the front can be executed independently in port 3001. To do so, go to the folder `client` and execute `npm start`.

To build the front, go to the folder client and execute `npm run build`, this will create inside `client` folder a `build` folder with all the generated code.

## Public folder

Once you have started the application, it will expose the chatbot client in http://localhost:<PORT>/ or http://localhost:<PORT>/index_speech.html

It includes 2 versions of client, the basic one and another version using Azure Speech for STT (Speech to text).
