import base64
import os
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ActivityTypes, Activity
from botbuilder.schema import ChannelAccount
from openai import AzureOpenAI



class EchoBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        print(f"on_message_activity called: {turn_context.activity.text}")
        if "view" in turn_context.activity.text.lower():
            event_activity = Activity(
                type=ActivityTypes.event,
                name="makeScreenshot",
                value={"key": "value"}
            )
            await turn_context.send_activity(event_activity)

        return await turn_context.send_activity(
            MessageFactory.text(f"Echo: {turn_context.activity.text}")
        )
    
    async def on_event_activity(self, turn_context):
        imgGenerated = turn_context.activity.value.get("img", None)

        # TODO:  in utils.py there is a function to create the directory and save the image, but the import it is not working here. Needs investigation.
        # Remove the code below and use the function from utils.py
        cwd = os.getcwd()
        directory = f"{cwd}/public/imagesSaved"
        os.makedirs(directory, exist_ok=True)
        
        imageCleaned = imgGenerated.replace("data:image/png;base64,", "")
        if imageCleaned:
            img_bytes = base64.b64decode(imageCleaned)
            with open(f"{directory}/screenShotPoc.png", "wb") as img_file:
                img_file.write(img_bytes)
    
        client = AzureOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),  
            api_version=os.environ.get("OPENAI_API_VERSION"),
            base_url=f"{os.environ.get('OPENAI_API_BASE')}/openai/deployments/{os.environ.get('OPENAI_DEPLOYMENT_NAME')}"
        )

        response = client.chat.completions.create(
            model=f"{os.environ.get('OPENAI_DEPLOYMENT_NAME')}",
            messages=[
            { "role": "system", "content": "You are a very patient childcare nurse." },
            {
                "role": "user",
                "content": [
                {"type": "text", "text": "Explain to a child what's in this image. Avoid describing and listing individual elements."},
                {
                    "type": "image_url",
                    "image_url": {
                    "url": imgGenerated,
                    },
                },
                ],
            }
            ],
            max_tokens=2000,
        )

        message = response.choices[0].message.content
        
        return await turn_context.send_activity(
            MessageFactory.text(message)
        )
