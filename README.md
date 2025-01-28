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


## Export .ENV to Azure WebAPP

### Generate the current settings.json
az webapp config appsettings list --name acc-poc-web-app-svc-test-01 --resource-group z-ago-airesearchsb01-ew-01 > settings.json

### Run the script
/bin/bash export_settings_json.sh  

### Set the new environment variables to WebAPP
From local, run this command:
```
az webapp config appsettings set --name acc-poc-web-app-svc-test-01 --resource-group z-ago-airesearchsb01-ew-01 --settings @settings.json
```

## Deploy

From local, run this command:
```
az webapp up --sku B1 --logs  --resource-group z-ago-airesearchsb01-ew-01 --plan ASP-acc-poc-web-app-svc-test-01-8e42 --location westeurope --runtime PYTHON:3.12 --name acc-poc-web-app-svc-test-01 --verbose
```
