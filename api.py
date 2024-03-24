from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from code_generator import open_ai_code_generator
class UserRequest(BaseModel):
    query: str

app = FastAPI()


# Allow requests only from http://localhost:5500
# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message" : "App is up and running"}


@app.post("/api/code_generator")
async def code_generator(user_request : UserRequest):

    # Hit OpenAI
    resp = open_ai_code_generator(user_prompt=user_request.query)

    return {"code_snippet" : resp}