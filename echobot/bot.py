import os
from .openapi_utils import describe_image
from .openapi_agent_utils import agent_describe_image
from .utils import save_image    
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ActivityTypes, Activity
from botbuilder.schema import ChannelAccount
from openai import AzureOpenAI




class EchoBot(ActivityHandler):
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),  
            api_version=os.environ.get("OPENAI_API_VERSION"),
            base_url=f"{os.environ.get('OPENAI_API_BASE')}/openai/deployments/{os.environ.get('OPENAI_DEPLOYMENT_NAME')}"
        )

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

        # Save the image to the public/generatedScreenshots folder
        save_image(imgGenerated, "public/generatedScreenshots", "screenShotPoc.png")

        # Use the openai API to describe the image
        response = describe_image(imgGenerated, self.client)
        message = response.choices[0].message.content

        # Use the openai agent to describe the image
        # TODO: It is not working error 'AttributeError: 'AzureOpenAI' object has no attribute 'parent_run_id' needs to be investigated
        #agent_response= agent_describe_image(imgGenerated, self.client)
        #print(f"agent result: {agent_response.choices[0].message.content}")
        
        return await turn_context.send_activity(
            MessageFactory.text(message)
        )
