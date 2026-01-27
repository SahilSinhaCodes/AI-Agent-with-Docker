from fastapi import APIRouter, Depends
from sqlmodel import Session,select

from api.db import get_session
from .models import ChatMessagePayload, ChatMessage

router = APIRouter()

# /api/chats/
@router.get("")
def chat_health():
    return {"status": "ok"}

@router.get("/recent/")
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage) # sql -> query
    results = session.exec(query).fetchall()[:10]
    return results

# HTTP POST -> payload = {"message": "Hello world"} -> {"message": "hello world", "id": 1}
@router.post("", response_model=ChatMessage)
def chat_create_message(
        payload:ChatMessagePayload,
        session: Session = Depends(get_session)
):
    data = payload.model_dump() # pydantic -> dict
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj) # ensure id/primary key added to the obj instance
    # ready to store in the database
    return obj