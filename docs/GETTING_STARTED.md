# 🚀 Getting Started with Agent Core

> **Prerequisites**
> *   **Ollama** (Installed & Running `ollama serve`)
> *   **Redis** (Optional, falls back to memory if missing)
> *   **Python 3.11+**

## 1. Environment Setup

### A. Start Local LLM
Ensure you have the model pulled:
```bash
ollama pull llama3
# Verify it's running
curl http://localhost:11434/api/tags
```

### B. Start Helper Services (Redis)
```bash
docker-compose up -d
```

---

## 2. Installation & Execution

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Agent CLI
```bash
python main.py
```
*You will see an interactive prompt.*

---

## 3. Usage Guide

Interactive Session Example:

```text
> User: What is 25 * 4?
> Agent: [Thinking] I should use the calculator.
> Agent: [Action] Calculator(25 * 4)
> Agent: [Observation] 100
> Agent: The answer is 100.
```

### Adding New Tools
To extend the agent, simply define a function with type hints in `tools.py`.
```python
@tool
def get_weather(city: str) -> str:
    """Gets the weather for a city."""
    return "Sunny"
```
The Agent automatically detects and uses this tool.

---

## 4. Running Tests

### Unit Tests (Logic)
```bash
pytest tests/
```

### Integration Test (Full Loop)
This runs a predefined scenario to verify the ReAct loop resolves correctly.
```bash
python verify.py
```
