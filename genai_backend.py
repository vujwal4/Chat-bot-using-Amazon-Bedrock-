import os
from langchain_aws import ChatBedrock
from langchain_community.llms import Bedrock 
#from langchain_community.llms import Bedrock
from langchain_classic.memory import ConversationBufferMemory
#from langchain_community.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain

def chatbot():
    return ChatBedrock(
        credentials_profile_name="default",
        model_id="amazon.nova-lite-v1:0",
        model_kwargs={
            "temperature": 0.3,
            "top_p": 0.9,
            "max_gen_len": 400,
        },
    )

def chat_memory():
    llm_memo= chatbot()
    memory = ConversationBufferMemory(llm=llm_memo , max_token_limit=500)
    return memory

def chat_conversation(input_text , memory):
    llm_chain_data = chatbot()
    llm_conversation = ConversationChain(llm=llm_chain_data, memory= memory , verbose= True)
    chat_reply = llm_conversation.predict(input= input_text)
    return chat_reply 
