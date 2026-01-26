# 🎤 Interview Cheat Sheet: Agent Core

## 1. The Elevator Pitch (2 Minutes)

"Agent Core is a **Local AI Orchestration Engine** that turns static LLMs into autonomous agents.
It implements the **ReAct (Reason + Act) Pattern**, allowing the AI to 'Think' about a problem, 'Act' by calling Python functions (Tools), and 'Observe' the results before answering.
Instead of relying on cloud APIs like OpenAI Functions, I built this using **Ollama** and **LangChain** to run completely safely on local hardware, with **Redis** providing persistent memory across sessions."

---

## 2. "Explain Like I'm 5" (The Chef)

"Imagine a Chef (The AI).
*   **A normal Chatbot**: Is a Chef locked in an empty room. You ask for a cake, he *describes* a cake, but can't make one.
*   **Agent Core**: Is a Chef in a fully stocked kitchen.
*   **Tools**: He has a Stove (Calculator), a Fridge (Database), and a Recipe Book (Search).
*   **ReAct**: If you ask for a cake, he checks the fridge (Action), sees no eggs (Observation), decides to buy eggs (Thought), and then bakes it. He actually *does* things."

---

## 3. Tough Technical Questions

### Q: Why use ReAct vs just a chain of prompts?
**A:** "Flexibility.
A Chain is hard-coded: `Step 1 -> Step 2 -> Step 3`.
The ReAct loop is dynamic. If Step 1 fails, the Agent *sees* the error and can try a different approach (e.g., 'Google Search failed, let me try Wikipedia'). This autonomy allows it to solve undefined or messy problems."

### Q: How do you prevent the Agent from looping forever?
**A:** "I implement a **Max Iteration Limit** (typically 5 steps).
If the agent hasn't found the answer after 5 actions, the loop is hard-terminated to prevent CPU waste.
I also use **Temperature 0** for the Tool Selection step to ensure deterministic, logical choices, preventing it from getting 'creatively distracted'."

### Q: How does Local Llama 3 compare to GPT-4 for agents?
**A:** "It's faster but dumber.
GPT-4 follows complex JSON schemas perfectly. Llama 3 8B sometimes forgets to close a bracket or hallucinates a tool name.
To fix this, I implemented a **Self-Correction Layer**: If the JSON parsing fails, I feed the error stack trace *back* into the Context so the model can see its mistake and retry formatting. This reliability engineering makes small models viable."
