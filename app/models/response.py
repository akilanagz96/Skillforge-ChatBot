from pydantic import BaseModel


class ChatResponse(BaseModel):
    answer: str
    show_lead_popup: bool = False