import os
import sys
import traceback
from datetime import datetime
from http import HTTPStatus
import httpx
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity, ActivityTypes


from echobot.bot import EchoBot


load_dotenv() 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bot_settings = BotFrameworkAdapterSettings(
    app_id=os.environ.get("BOT_ID"), 
    app_password=os.environ.get("BOT_PASSWORD")
)
bot_adapter = BotFrameworkAdapter(bot_settings)



# Catch-all for errors.
async def on_error(context: TurnContext, error: Exception):
    # This check writes out errors to console log .vs. app insights.
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity(
        "To continue to run this bot, please fix the bot source code."
    )
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":
        # Create a trace activity that contains the error object
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        # Send a trace activity, which will be displayed in Bot Framework Emulator
        await context.send_activity(trace_activity)


echo_bot = EchoBot()

bot_adapter.on_turn_error = on_error

@app.post('/api/speechservices/token')
async def get_speech_token():
    try:
        headers = {
            'Ocp-Apim-Subscription-Key': os.environ.get("SPEECH_SVC_KEY"),
            'Content-Type': 'application/json'
        }
        response = httpx.post(f'https://{os.environ.get("SPEECH_REGION")}.api.cognitive.microsoft.com/sts/v1.0/issueToken', headers=headers)

        if response.status_code == 200:
            data = response.text
            print('Speech token:', data)
        else:
            print(f'Error {response.status_code}: {response.text}')

        return {
            "authorizationToken": data,
            "region": os.environ.get("SPEECH_REGION")
        }
    except Exception as e:
        print(f"Error generating Speech token: {str(e)}")
        return {"error": "Failed to generate Speech token"}, 500

@app.post('/api/directline/token')
async def get_token():
    try:
        headers = {
            'Authorization': f'Bearer {os.environ.get("BOT_SECRET")}',
            'Content-Type': 'application/json'
        }
        response = httpx.post('https://directline.botframework.com/v3/directline/tokens/generate', headers=headers)

        if response.status_code == 200:
            data = response.json()
            print('Generated token:', data)
        else:
            print(f'Error {response.status_code}: {response.text}')

        return data
    except Exception as e:
        print(f"Error generating Direct Line token: {str(e)}")
        return {"error": "Failed to generate Direct Line token"}, 500

@app.post("/api/messages")
async def messages(request: Request):
    body = await request.json()
    activity = Activity().deserialize(body)

    auth_header = request.headers.get("Authorization", "")
    response = await bot_adapter.process_activity(activity, auth_header, echo_bot.on_turn)
    return response


@app.get("/api/getConfig")
async def get_config():
    config = {
        "domain": os.environ.get("DOMAIN"),
        "port": os.environ.get("PORT"),
    }
    return config

@app.get("/")
async def read_index():
    return FileResponse("client/build/index.html")

app.mount("/", StaticFiles(directory="client/build"), name="public")

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="localhost", port=int(os.environ.get("PORT")), reload=True, log_level="debug")
    except Exception as error:
        raise error