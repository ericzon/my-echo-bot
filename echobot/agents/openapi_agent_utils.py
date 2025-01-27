import os
from .agent_utils import create_agent
from ..openapi_utils import describe_image
from langchain_openai import ChatOpenAI


def agent_describe_image(image, client):
    model = ChatOpenAI(model="gpt-4o")
    tool_describe_image = {
        'name': 'Describe Image',
        'function': describe_image,
        'arguments': {'image_data': {'type': 'string', 'description': 'The image data in base64 format to describe'}, 'client': {'type': 'object', 'description': 'The OpenAPI client'}},
    }
    tools = [tool_describe_image]
    agent_executor = create_agent(model, tools)
    print(f"agent_executor: {agent_executor}")
    return agent_executor.invoke(tool_describe_image, {'image_data': image, 'client': client})

