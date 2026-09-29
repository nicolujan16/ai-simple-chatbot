# LangGraph Tutorial

[Read in English](README.md)

Un chatbot simple de terminal hecho con [LangGraph](https://github.com/langchain-ai/langgraph) mientras aprendo la librería. Usa un LLM a través de [OpenRouter](https://openrouter.ai/), puede buscar en la web con [Tavily](https://tavily.com/) y recuerda la conversación durante la sesión.

## Requisitos

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- Una API key de OpenRouter y una de Tavily

## Instalación

```bash
git clone https://github.com/nicolujan16/ai-simple-chatbot.git
cd langGraph-tutorial
uv sync
```

Copiá `.env.example` a `.env` y completá tus keys:

```
TAVILY_API_KEY=your_tavily_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

## Uso

```bash
uv run main.py
```

Escribí tus mensajes después de `User:`. Para salir, escribí `quit`, `exit` o `q`.

## Estructura del proyecto

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Punto de entrada |
| `chat.py` | Loop del chat en la terminal |
| `graph.py` | Definición del grafo (nodo chatbot + nodo de tools) |
| `state.py` | Estado del grafo |
| `config.py` | Configuración del LLM, las tools y la memoria |
