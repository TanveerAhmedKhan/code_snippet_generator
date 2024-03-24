
import os
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

import html
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()
openai_key = os.getenv('openai_key')
openai_org = os.getenv('org_key')


chat = ChatOpenAI(temperature=0, openai_api_key=openai_key, openai_organization=openai_org)

messages = [
    SystemMessage(
        content="""
        As a state-of-the-art code snippet generator, your expertise spans across all programming languages, consistently adhering to the highest industry standards.
        Your sole purpose is to craft code blocks that meet the user's specified programming language requirements.
        Ensure that your responses are EXCLUSIVELY composed of code blocks, devoid of any additional text or instructions."""
    )
]

def open_ai_code_generator(user_prompt : str) -> str:
  
  messages.append(HumanMessage(content=user_prompt))
  openai_resp = chat.invoke(messages)

  html_code = html.escape(openai_resp.content)

  html_formatted = f"<pre>{html_code}</pre>"

  return html_formatted