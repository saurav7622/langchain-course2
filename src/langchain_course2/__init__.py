from dotenv import load_dotenv
import os

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()




llm = ChatOpenAI(    model="gpt-5",temperature=0.1)
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)

def main() -> None:
    print("Hello from langchain-course2!")
    result =agent.invoke({"messages":HumanMessage(content="search for 3 job positings for an ai engineer using langchain in gurugram,India in linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()