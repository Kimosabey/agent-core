# 🏗️ System Architecture

## 🔍 Overview
The **Local AI Agent (A2)** is designed as an autonomous reasoning engine that bridges the gap between static LLMs and dynamic database actions.

![Architecture Diagram](assets/architecture_diagram.png)

## 🧩 Core Components

### 1. 🧠 Agent Router (LangChain)
The central nervous system of the application. It receives user inputs and decides:
- **Do I need more info?** -> Query Redis for context.
- **Do I need to check the database?** -> Use SQL Tools.
- **Can I answer now?** -> Generate direct response.

### 2. 🛡️ Reasoning Engine (ReAct Pattern)
We use the **Reason + Act** loop to ensure accuracy:
1.  **Reason**: Analyze the user's request.
2.  **Act**: Execute a specific tool (e.g., `execute_sql_query`).
3.  **Observe**: Look at the data returned.
4.  **Answer**: Formulate the final response.

![ReAct Flow](assets/react_flow_diagram.png)

### 3. 💾 Long-Term Memory (Redis)
Unlike standard chatbots, A2 remembers.
- Stores conversation history.
- Retrieves past interactions to maintain context.
- Fast, key-value storage for low latency.

### 4. 🧰 Tools & Skills (SQLite/SQL)
The agent is equipped with "skills" to interact with the real world:
- `list_tables`: Awareness of data structure.
- `execute_sql_query`: Ability to fetch live data.

## 🚀 Tech Stack
- **Framework**: LangChain, LangGraph
- **LLM**: GPT-4o-mini (OpenAI) / Llama 3 (Ollama)
- **Database**: SQLite (Mock Data), Redis (Memory)
- **UI**: Rich CLI (Python)
