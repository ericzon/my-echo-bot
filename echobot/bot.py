from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ActivityTypes, Activity
from botbuilder.schema import ChannelAccount


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
        img_property = turn_context.activity.value.get("img", None)
        print(f"on_message_event called img received: {img_property}")
        # TODO: Call the API to get the description of the image
        return await super().on_event_activity(turn_context)