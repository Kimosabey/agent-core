# Local AI Agent (A2)
## Agentic AI Orchestration Layer

<div align="center">

![Status](https://img.shields.io/badge/Status-Parked-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**Tech Stack**

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge)
![Redis](https://img.shields.io/badge/Redis-Memory-DC382D?style=for-the-badge&logo=redis&logoColor=white)

**Features**

![ReAct Pattern](https://img.shields.io/badge/Pattern-ReAct-FF6B6B?style=flat-square)
![Tool Use](https://img.shields.io/badge/Capability-Tool_Use-4ECDC4?style=flat-square)
![Context Awareness](https://img.shields.io/badge/Feature-Context_Awareness-95E1D3?style=flat-square)

</div>

---

## 🚀 Quick Start

### 1. Prerequisites
- **Ollama** (Running locally with `llama3` or `mistral`)
- **Redis** (Docker or Local)
- **Python 3.10+**

### 2. Installation
```bash
git clone <your-repo>
cd agent-core
pip install -r requirements.txt
```

### 3. Run Agent
```bash
# Ensure Ollama & Redis are up
python main.py
```

---

## 📸 Visual Overview

### System Data Flow
![System Architecture](docs/assets/architecture_diagram.png)
*Flow of prompts through Router, Memory, and Tools*

### ReAct Pattern Logic
![ReAct Pattern Flow](docs/assets/react_flow_diagram.png)
*Reason-Act loops for solving complex queries*

---

## ✨ Key Features

### 🧠 Autonomous Reasoning
- **ReAct Pattern**: Implements "Reason + Act" loops to decompose complex user queries into actionable steps.
- **Chain-of-Thought**: Maintains internal monologue to guide decision-making.

### 🛠️ Tool Orchestration
- **Function Calling**: Capable of executing specific python functions (mock DB queries, calculations).
- **Dynamic Selection**: Router selects the best tool for the job.

### 🧠 Persistent Memory
- **Context Awareness**: Uses Redis to store conversation history, allowing for multi-turn dialogue with context retention.

---

## 🏗️ Architecture

```mermaid
graph LR
    User[User Prompt] --> Router[Agent Router]
    Router -->|Context Lookup| Redis[(Redis Memory)]
    Router -->|Action Decision| Tools[Tool Execution]
    Tools -->|Query Results| Router
    Router -->|Final Generative Response| LLM[LLM Response]
```

---

## 🔧 Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Logic** | Python | Core application runtime |
| **Framework** | LangChain | Agent orchestration & prompts |
| **LLM** | Ollama | Local inference runner |
| **Memory** | Redis | Vector/Conversation store |

---

## 📚 Documentation

- [**Architecture Guide**](./docs/ARCHITECTURE.md) - System design and patterns

---

## 📝 License

MIT License - See [LICENSE](./LICENSE) for details

---

## 👤 Author

**Harshan Aiyappa**  
Senior Full-Stack Engineer  
📧 [GitHub](https://github.com/Kimosabey)

---

**Built with**: Python • LangChain • Ollama • Redis
