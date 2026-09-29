from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition
from config import tools, memory, llm_with_tools
from state import State

def build_graph() -> StateGraph:
    graph_builder = StateGraph(State)

    def chatbot(state: State):
        message = llm_with_tools.invoke(state["messages"])
        return {"messages": [message]}

    graph_builder.add_node("chatbot", chatbot) # NODO DEL CHAT

    tool_node = ToolNode(tools)
    graph_builder.add_node("tools", tool_node) # NODO DE LAS TOOLS

    graph_builder.add_conditional_edges("chatbot", tools_condition) # ACA CONECTAMOS EL LLM CON EL TOOL NODE

    graph_builder.add_edge("tools", "chatbot") # CONECTAMOS LAS TOOLS PARA QUE PUEDA VOLVER AL LLM

    graph_builder.add_edge(START, "chatbot") # DEFINIMOS DONDE COMIENZA EL GRAFO, EN EL CHATBOT (LLM)

    return graph_builder.compile(checkpointer=memory) # COMPILAMOS EL GRAFO COMPLETO CON MEMORIA AGREGADA