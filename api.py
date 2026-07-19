from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from core.llm import LLM
from core.session import ChatSession
from tools.manager import ToolManager

app = FastAPI(title="Jarvis API", version="0.1.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global instances
llm = LLM()
tool_manager = ToolManager()

# In-memory session storage (for demo - use Redis/DB in production)
sessions = {}


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    session_id: str


class SessionCreateResponse(BaseModel):
    session_id: str
    message: str


@app.get("/")
async def root():
    return {"message": "Jarvis API is running", "version": "0.1.0"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Send a message to Jarvis and get a response."""
    # Get or create session
    if request.session_id and request.session_id in sessions:
        session = sessions[request.session_id]
    else:
        session = ChatSession()
        request.session_id = str(id(session))
        sessions[request.session_id] = session
    
    # Try to route to a tool
    tool_result = tool_manager.route(request.message)
    
    if tool_result and tool_result.success:
        reply = tool_result.content
    else:
        # Use LLM
        session.add_user_message(request.message)
        reply = llm.ask(session.messages)
        session.add_assistant_message(reply)
    
    return ChatResponse(reply=reply, session_id=request.session_id)


@app.post("/sessions", response_model=SessionCreateResponse)
async def create_session():
    """Create a new chat session."""
    session = ChatSession()
    session_id = str(id(session))
    sessions[session_id] = session
    return SessionCreateResponse(session_id=session_id, message="Session created")


@app.delete("/sessions/{session_id}")
async def delete_session(session_id: str):
    """Delete a chat session."""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    del sessions[session_id]
    return {"message": "Session deleted"}


@app.post("/sessions/{session_id}/clear")
async def clear_session(session_id: str):
    """Clear a session's conversation history."""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    sessions[session_id].clear()
    return {"message": "Session cleared"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
