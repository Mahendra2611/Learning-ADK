from google.adk.agents import Agent
from datetime import datetime
from google.adk.tools import google_search

def get_current_time()->dict:
    # this is doc string which tell the agent what does this tool is doing
    """
    Get the current time in format YYYY-MM-DD HH:MM:SS
    """
    # while returning the value, do not just return value, write its meaning or format also
    return {
        "current_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name = "tool_agent",
    model = "gemini-2.0-flash",
    # description is helpfull when we have multiple agents, other agents get to know what does this agent is doing
    description="Tool agent",
    # instruction is used to set the default prompt, tone, personality and behaviour
    instruction="""
You are helpful assistant that can use the following tools : - 
get_current_time
""",
# you can only use one tool at a time
#tools=[google_search,get_current_time]  -> it doesnot work

#tools=[google_search]
tools=[get_current_time]
)