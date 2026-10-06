import requests
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent


# 1. DEFINE THE TOOL

@tool
def check_machine_status(machine_id: str) -> str:
    """
    Check recent operational status and torque values 
    of a specific manufacturing machine. 
    Input should be the machine_id like 'MCH-01'.
    """
    try:
        response = requests.get(
            f"http://api:8000/api/machine_status?machine_id={machine_id}
        )
        return str(response.json())
    except Exception as e:
        return f"Error fetching data: {str(e)}"


@tool
def get_all_machines() -> str:
    """Get a list of all machines we have data for."""
    try:
        response = requests.get("http://api:8000/api/all_machines")
        return str(response.json())
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def get_error_summary() -> str:
    """Get a summary of all errors across all machines."""
    try:
        response = requests.get("http://api:8000/api/errors")
        return str(response.json())
    except Exception as e:
        return f"Error: {str(e)}"    



# 2. SET UP OLLAMA LLM

llm = ChatOllama(model="llama3.2", temperature=0)



# 3. BUILD THE AGENT (using langgraph)

tools = [check_machine_status, get_all_machines, get_error_summary]
agent = create_react_agent(llm, tools)



# 4. RUN IT

if __name__ == "__main__":
    print("\n Starting Manufacturing Data Agent...\n")
    
    query = "Check machine MCH-01 and tell me if there are any errors in the torque values."
    
    result = agent.invoke({"messages": [("user", query)]})

    print("\n Agent's reasoning process:")
    for msg in result["messages"]:
       print(f"- {msg.type}: {msg.content}")
    print("\n Final Answer:")
    print(result["messages"][-1].content)