from typing import TypedDict

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END

load_dotenv()

class MoodState(TypedDict):
    input: str
    mood: str
    response: str

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

def detect_mood_llm(state: MoodState):
    prompt = f"""
    Todo
    Message: {state['input']}
    """

    result = llm.invoke(prompt).content.strip().lower()
    state["mood"] = result
    return state

def comfort_node(state: MoodState):
    state["response"] = "Todo"
    return state

def hype_node(state: MoodState):
    state["response"] = "Todo"
    return state

def neutral_node(state: MoodState):
    state["response"] = "Todo"
    return state

def route(state: MoodState):
    return state["mood"]

builder = StateGraph(MoodState)
builder.add_node("detect_mood", detect_mood_llm)
builder.add_node("comfort", comfort_node)
builder.add_node("hype", hype_node)
builder.add_node("neutral", neutral_node)

builder.set_entry_point("detect_mood")

builder.add_conditional_edges(
#Todo
)

builder.add_edge("comfort", END)
builder.add_edge("hype", END)
builder.add_edge("neutral", END)

graph = builder.compile()

if __name__ == "__main__":
    user_input = input("Todo")
    result = graph.invoke({"input": user_input})
    print("\nResponse:", result["response"])