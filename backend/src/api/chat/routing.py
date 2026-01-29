from fastapi import APIRouter, Depends
from sqlmodel import Session,select
from typing import List
from api.db import get_session
from api.ai.schemas import EmailMessageSchema
from api.ai.services import generate_email_message
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem

router = APIRouter()

# /api/chats/
@router.get("")
def chat_health():
    return {"status": "ok"}

@router.get("/recent/",response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage) # sql -> query
    results = session.exec(query).fetchall()[:10]
    return results

# HTTP POST -> payload = {"message": "Hello world"} -> {"message": "hello world", "id": 1}
# curl -X POST -d '{"message": "Give me a summary of why it's good to go outside"}' -H "Content-Type: application/json" http://localhost:8080/api/chats/

@router.post("", response_model=EmailMessageSchema)
def chat_create_message(
        payload:ChatMessagePayload,
        session: Session = Depends(get_session)
):
    data = payload.model_dump() # pydantic -> dict
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    # session.refresh(obj) # ensure id/primary key added to the obj instance
    # ready to store in the database
    response = generate_email_message(payload.message)
    return response