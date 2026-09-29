import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver

# Setup Inicial
load_dotenv() # Load environment variables from a .env file
memory = MemorySaver()  # Initialize memory saver for storing conversation history
tavily_tool = TavilySearch(max_results=2)  # Initialize Tavily search tool for retrieving information
tools = [tavily_tool]  # List of tools to be used in the application

llm = init_chat_model(
    "openai/gpt-4o-mini", # nombre del modelo en formato OpenRouter
    model_provider="openai", # usa el cliente de OpenAI (compatible)
    base_url="https://openrouter.ai/api/v1", # apunta a OpenRouter en vez de OpenAI
    api_key=os.getenv("OPENROUTER_API_KEY"), # tu key de OpenRouter
)
llm_with_tools = llm.bind_tools(tools)  # Bind the tools to the language model for enhanced capabilities

graph_config = { "configurable": {"thread_id": "1"} }

