from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ActivityTypes, Activity
from botbuilder.schema import ChannelAccount
from openai import OpenAI



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
        print(f"on_message_event called img received: {imgGenerated}")

        # TODO: Call the corresponding API to get the description of the image. Below the code commented would be a first approach using gpt-4o-mini,
        # but we need the api_key client to be able to do the call, we can use a OPENAI_API_KEY environment variable. 
        """ client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
            {
                "role": "user",
                "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                    "url": imgGenerated,
                    },
                },
                ],
            }
            ],
            max_tokens=300,
        )
        print(response.choices[0]) """
        return await super().on_event_activity(turn_context)