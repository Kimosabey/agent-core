from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
# form langchain.agents import create_tool_calling_agent, AgentExecutor # Deprecated/Unused
from langgraph.prebuilt import create_react_agent

from langchain_core.runnables.history import RunnableWithMessageHistory
from .config import Config
from .tools import list_tables, describe_table, execute_sql_query
from .memory import get_redis_history

from langchain_openai import ChatOpenAI

def get_agent_executor():
    # 1. Initialize LLM
    if Config.LLM_PROVIDER == "openai":
        print(f"🤖 Using OpenAI Model: {Config.OPENAI_MODEL}")
        llm = ChatOpenAI(
            model=Config.OPENAI_MODEL,
            temperature=0,
            api_key=Config.OPENAI_API_KEY
        )
    else:
        print(f"🦙 Using Ollama Model: {Config.OLLAMA_MODEL} at {Config.OLLAMA_BASE_URL}")
        llm = ChatOllama(
            model=Config.OLLAMA_MODEL, 
            temperature=0,
            base_url=Config.OLLAMA_BASE_URL
        )

    # 2. Define Tools
    tools = [list_tables, describe_table, execute_sql_query]

    # 3. Create Agent
    # New way with LangGraph's prebuilt ReAct agent is often preferred for simplicity, 
    # but let's strictly follow the specific "Agent Router" flow if possible.
    # Actually, create_react_agent from langgraph.prebuilt is the most robust "modern" way.
    
    agent_executor = create_react_agent(llm, tools)

    # 4. Wrap with Memory
    # We need to manage state manually or use RunnableWithMessageHistory if NOT using LangGraph's checkpointer.
    # Since we are using an external Redis for memory lookup as per the diagram:
    # [Agent Router] -> (Lookup) -> [Redis Memory]
    
    agent_with_chat_history = RunnableWithMessageHistory(
        agent_executor,
        get_redis_history,
        input_messages_key="messages",
        history_messages_key="history",
    )
    
    return agent_with_chat_history
