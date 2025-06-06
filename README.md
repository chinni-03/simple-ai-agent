# 🧠 Simple AI Assistant

A minimal AI assistant built using [LangChain](https://www.langchain.com/), [OpenAI](https://platform.openai.com/), and [UV](https://astral.sh/blog/uv/), designed to perform basic conversations and tasks like calculations and greetings via tool integration.

---

## 🚀 Features

- Streamed interaction with OpenAI-powered assistant
- ReAct-style agent (reason and act) using LangGraph
- Supports custom tools like:
  - Calculator
  - Personal greeting

---

## 🛠 Prerequisites

Ensure the following tools are installed:

- [Visual Studio Code](https://code.visualstudio.com/)
- [UV package manager](https://docs.astral.sh/uv/#installation)
- A valid [OpenAI API key](https://platform.openai.com/account/api-keys)

---

## 📁 Setup Instructions

### 1. Clone or Create the Project

```bash
mkdir ai-agent
cd ai-agent
uv init .
```

### 2. Install Dependencies

```bash
uv add langgraph langchain python-dotenv langchain-openai
```

### 3. Add Environment Variables

Create a `.env` file in your project directory:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. Create Your Main Python File

Create `main.py` and paste the code below (see [Usage](main.py)).

---

## 🧩 Usage

Run the project:

```bash
uv run main.py
```

Type messages to chat with the assistant.  
Type `quit` to exit the program.

---

## 🧪 Sample Tools

Here are two example tools integrated into the assistant:

```python
@tool
def calculator(a: float, b: float) -> str:
    """Performs addition of two numbers."""
    return f"The sum of {a} and {b} is {a + b}"

@tool
def say_hello(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}! Hope you're doing great."
```

You can easily add more tools following this format.

---

## 🧼 Example Output

```bash
You: Add 10 and 5

Assistant: The sum of 10 and 5 is 15

You: Say hello to Harshini

Assistant: Hello, Harshini! Hope you're doing great.
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [OpenAI](https://platform.openai.com/)
