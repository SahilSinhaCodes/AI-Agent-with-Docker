from api.ai.llms import get_openai_llm
from api.ai.schemas import EmailMessageSchema

def generate_email_message(query: str) -> EmailMessageSchema:
    llm_base = get_openai_llm()

    # Keep using json_mode for Groq compatibility
    llm = llm_base.with_structured_output(EmailMessageSchema, method="json_mode")

    messages = [
        (
            "system",
            "You are a helpful assistant. You must output your response in valid JSON format with the keys: 'subject', 'contents', and 'invalid_request'.\n\n"
            "CRITICAL RULES:\n"
            "1. The 'contents' field MUST be a single, plain text string.\n"
            "2. Do NOT use objects, lists, arrays, or bullet points inside 'contents'.\n"
            "3. If you have steps or lists, format them as a plain text paragraph or use dashes in a string."
        ),
        ("human", query),
    ]

    return llm.invoke(messages)