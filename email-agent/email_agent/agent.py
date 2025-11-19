from google.adk.agents import Agent
from pydantic import BaseModel,Field

class EmailContent(BaseModel):
    subject:str = Field(
        description="The subject line of the email. Should be concise and descriptive"
    )
    body:str = Field(
        description="The main content of the email. Should be well formated with proper greeting, paragraphs and sign off"
    )


root_agent = Agent(
    name = "email_agent",
    model = "gemini-2.0-flash",
    # description is helpfull when we have multiple agents, other agents get to know what does this agent is doing
    description="Generate professional email with structure body and subject",
    # instruction is used to set the default prompt, tone, personality and behaviour
    instruction="""
You are an Email Generation Assistant.
Your task is to generate a professional email based on user's request.
follow these points :
- clean and concise content
- appropriate closing
- your name is signature
- email should match the purpose (formal for buiness, friendly for colleagues)
- keep email concise but complete
IMPORTANT : your response must be valid json matching this structure: 
{
"subject":"Subject line here,
"body":"Email body here with proper paragraphs and formatting",
}
DO NOT indclude any explanation or additional text outside the JSON response
""",
 output_schema=EmailContent,
 output_key="email",
)