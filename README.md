# Simple AI Chatbot

[Leer en español](README.es.md)

A simple terminal chatbot built with [LangGraph](https://github.com/langchain-ai/langgraph) while learning the library. It uses an LLM through [OpenRouter](https://openrouter.ai/), can search the web with [Tavily](https://tavily.com/), and remembers the conversation during the session.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- An OpenRouter API key and a Tavily API key

## Setup

```bash
git clone https://github.com/nicolujan16/ai-simple-chatbot.git
cd ai-simple-chatbot
uv sync
```

Copy `.env.example` to `.env` and add your keys:

```
TAVILY_API_KEY=your_tavily_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

## Usage

```bash
uv run main.py
```

Type your messages after `User:`. To exit, type `quit`, `exit` or `q`.

## Project structure

| File | Description |
|------|-------------|
| `main.py` | Entry point |
| `chat.py` | Chat loop in the terminal |
| `graph.py` | Graph definition (chatbot node + tools node) |
| `state.py` | Graph state |
| `config.py` | LLM, tools and memory setup |
