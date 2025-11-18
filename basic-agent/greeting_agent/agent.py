from google.adk.agents import Agent

root_agent = Agent(
    name = "greeting_agent",
    model = "gemini-2.0-flash",
    # description is helpfull when we have multiple agents, other agents get to know what does this agent is doing
    description="Greeting agent",
    # instruction is used to set the default prompt, tone, personality and behaviour
    instruction="""
You are a helpful assistant that greets the user. 
Ask for the user's name and greet them by name
""",
)