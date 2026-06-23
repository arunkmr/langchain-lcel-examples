import os
from dotenv import load_dotenv
load_dotenv()

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq

model = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

from langchain_core.messages import HumanMessage,SystemMessage

messages =[
    SystemMessage(content="Translate the following from English to Tamil"),
    HumanMessage(content ="Hello How r you ?" )
]

result = model.invoke(messages)

from langchain_core.output_parsers import StrOutputParser 
parser = StrOutputParser()
print(parser.invoke(result))

#using LCEL we can chain the components

chain = model | parser

chain.invoke(messages)

###prompt templates

from langchain_core.prompts import ChatPromptTemplate
generic_template ='Translate the following into {language}:'

prompt = ChatPromptTemplate.from_messages(
    [("system", generic_template), ("user","{text}")]
)

result  = prompt.invoke({"language":"Tamil", "text":"Hello"})
result.to_messages()

chain = prompt | model | parser

print(chain.invoke({"language":"Tamil", "text":"Hello"}))
