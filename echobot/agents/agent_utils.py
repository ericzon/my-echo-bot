
from langgraph.prebuilt import create_react_agent

def create_agent(model, tools):
 agent_executor = create_react_agent(model, tools)
 return agent_executor
