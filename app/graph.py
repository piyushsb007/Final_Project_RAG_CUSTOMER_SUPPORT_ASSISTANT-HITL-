from typing import TypedDict,List
from langgraph.graph import StateGraph,START,END
from langgraph.types import interrupt
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from app.retriever import get_retriever

# load env variable
load_dotenv()

# Initialize llm 
llm = ChatGroq(
    model= "llama-3.1-8b-instant",
    api_key= os.getenv("GROQ_API_KEY")
)

# Define State
class AgentState(TypedDict):
    query : str
    context : str
    response : str
    category : str
    history: List[str]

# Defining Nodes functionality
def retrieve(state:AgentState):
    retrieve = get_retriever()

    docs = retrieve.invoke(state["query"])

    # Combing all retrieved chunks into one string
    context = "\n".join([doc.page_content for doc in docs])

    return {**state, "context" : context}

def process(state:AgentState):
    # if no context found escalate
    if not state["context"].strip():
        return{
            **state,
            "category" : "escalate",
            "response":"No relevant inforamtion found. Escalating..."
        }
    
    history_text = "\n".join(state.get("history", []))

    prompt = f"""
    You are a Customer Support Assistant.

    RULES:
    - Use ONLY the provided context
    - If answer is not in context -> reply ONLY: ESCALATE

    Context:
    {state['context']}

    Question:
    {state['query']}
    """
    answer = llm.invoke(prompt).content

    # if llm indicates uncertainty -> escalate
    if "ESCALATE" in answer.upper():
        return{
            **state,
            "category" : "escalate",
            "response" : "Escalating to human expert..."
        }

    return{
        **state,
        "category" : "support",
        "response" : answer
    }

# Human in the loop
def human(state:AgentState):
    print("⚠️ Escalation triggered")

    human_response = input("👨 Human Agent, enter response: ")

    return{
        **state,
        "response" : f"Human Expert: {human_response}"
    }

# Routing logic 
def route(state:AgentState):
    return "human" if state["category"] == "escalate" else "end"

# Build langgraph workflow
def build_graph():
    
    builder = StateGraph(AgentState)

    builder.add_node("retrieve",retrieve)
    builder.add_node("process",process)
    builder.add_node("human",human)

    #define flow
    builder.add_edge(START,"retrieve")
    
    builder.add_edge("retrieve","process")

    builder.add_conditional_edges(
        "process",
        route,{
            "human":"human",
            "end" : END
        }
    )
    builder.add_edge("human",END)

    return builder.compile() 


"""
This is the brain of your system:
- Retrieval
- Processing
- Decision making
- HITL escalation
"""