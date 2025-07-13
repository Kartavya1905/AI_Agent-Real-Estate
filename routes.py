from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.llm.agent import get_llm_response

router = APIRouter()

# Define input model
class ChatRequest(BaseModel):
    message: str

# Route for chat
@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    try:
        return get_llm_response(request.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
