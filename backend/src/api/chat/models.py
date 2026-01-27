from sqlmodel import SQLModel, Field

class ChatMEssagePayLoad(SQLModel):
    # pydantic model
    # validation
    message:str


class ChatMessage(SQLModel,table=True):
    # database table
    # saving,updating,getting,deleting
    id: int | None = Field(default=None,primary_key=True)
    message:str
