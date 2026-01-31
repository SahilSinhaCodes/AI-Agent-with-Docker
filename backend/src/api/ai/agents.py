from langgraph.prebuilt import create_react_agent
from api.ai.llms import get_openai_llm

from api.ai.tools import (
    send_me_email,
    get_unread_emails
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
        prompt="You are a helpful assistant for managing my email inbox for generating, sending, and reviewing emails."
    )

    return agent