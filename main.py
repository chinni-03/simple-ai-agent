from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Performs addition of two numbers."""
    return f"The sum of {a} and {b} is {a + b}"

@tool
def say_hello(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}! Hope you're doing great."

def main():
    model = ChatOpenAI(temperature=0)
    tools = [calculator, say_hello]
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("Try asking me to calculate something or greet you.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": HumanMessage(content=user_input)}
        ):
            if "agent" in chunk and "messages" in chunk['agent']:
                for message in chunk['agent']['messages']:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()