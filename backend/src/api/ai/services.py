from api.ai.llms import get_openai_llm
from api.ai.schemas import EmailMessageSchema

def generate_email_message(query: str) -> EmailMessageSchema:
    llm_base = get_openai_llm()

    # 1. method="json_mode" is correct for Llama-3.3 (JSON Object Mode)
    llm = llm_base.with_structured_output(EmailMessageSchema, method="json_mode")

    messages = [
        (
            "system",
            # 2. CRITICAL CHANGE: We must explicitly ask for JSON here.
            "You are a helpful assistant. You must output your response in valid JSON format matching the schema provided. Do not use markdown.",
        ),
        ("human", query),
    ]

    return llm.invoke(messages)