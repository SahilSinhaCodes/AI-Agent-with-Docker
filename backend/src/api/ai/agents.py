from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from api.ai.llms import get_openai_llm
from api.ai.tools import (
    send_me_email,
    get_unread_emails,
    research_email
)

EMAIL_TOOLS_LIST = [
    send_me_email,
    get_unread_emails
]

def get_email_agent():
    model = get_openai_llm()
    agent = create_react_agent(
        model=model,
        tools=EMAIL_TOOLS_LIST,
        # FIX: Explicitly tell it NOT to use transfer tools
        prompt=(
            "You are a helpful assistant for managing my email inbox. "
            "CRITICAL INSTRUCTION: You MUST use the 'send_me_email' tool to actually send emails. "
            "Do NOT just say you sent an email. Call the tool first. "
            "Only after the tool executes successfully should you reply to the user."
        ),
        name="email_agent"
    )

    return agent

def get_research_agent():
    model = get_openai_llm()
    agent = create_react_agent(
        model=model,
        tools=[research_email],
        # FIX: Strictly defined role + Anti-hallucination instruction
        prompt=(
            "You are a specialized email research assistant. "
            "You do NOT have access to the internet. You MUST use the 'research_email' tool to generate content. "
            "When you have the information, just output it as your final response. "
            "Do NOT try to call any tools named 'transfer' or 'supervisor'."
        ),
        name='research_agent'
    )

    return agent

def get_supervisor():
    llm = get_openai_llm()
    email_agent = get_email_agent()
    research_agent = get_research_agent()

    supe = create_supervisor(
        agents=[email_agent, research_agent],
        model=llm,
        prompt=(
            "You manage a research assistant and an email inbox manager. "
            "Assign work to them based on the user's request. "
            "When the job is done, simply reply to the user."
        )
    ).compile()
    return supe