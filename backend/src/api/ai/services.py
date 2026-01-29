from api.ai.llms import get_openai_llm
from api.ai.schemas import EmailMessageSchema

def generate_email_message(query: str) -> EmailMessageSchema:
    llm_base = get_openai_llm()

    # Keep using json_mode for Groq compatibility
    llm = llm_base.with_structured_output(EmailMessageSchema, method="json_mode")

    messages = [
        (
            "system",
            # CRITICAL FIX: We explicitly list the REQUIRED keys here.
            "You are a helpful assistant. You must output your response in valid JSON format with the keys: 'subject', 'contents', and 'invalid_request'. Do not use markdown.",
        ),
        ("human", query),
    ]

    return llm.invoke(messages)