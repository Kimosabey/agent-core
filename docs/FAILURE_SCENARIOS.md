# 🛡️ Failure Scenarios & Resilience

> "Agents are non-deterministic. They can loop forever or hallucinate."

This document details how Agent Core handles infinite loops, hallucinated tools, and context overflow.

## 1. Failure Matrix

| Component | Failure Mode | Impact | Recovery Strategy |
| :--- | :--- | :--- | :--- |
| **Logic Loop** | Infinite Thinking | **Critical**. Agent checks weather forever. | **Max Iterations**. The Executor hard-stops after 5 ReAct steps and forces a "I gave up" response. |
| **Tool Usage** | Hallucinated Tool | **Major**. Calls `get_bitcoin()` (doesn't exist). | **Exception Handling**. The system catches the `ValueError` and feeds it back to the LLM: "Tool not found, try again." |
| **Context** | Token Overflow | **Minor**. Crash on long chat. | **Memory Trimming**. Redis automatically keeps only the last `k=10` message pairs (FIFO). |

---

## 2. Deep Dive: Handling Hallucinations

### The Problem
Small models (like Llama 3 8B) sometimes invent tools.
*   **User**: "Check my email."
*   **Agent**: `Action: check_email()` (This function does not exist).

### The Solution: Self-Correction Loop
We do not crash. We return the error as an *Observation*.
1.  **Agent**: `check_email()`
2.  **System**: `Observation: Error: Tool 'check_email' not found. Available tools: [calculator, search].`
3.  **Agent**: "[Thought] Ah, I cannot check email. I will tell the user I can't do that."
4.  **Final**: "I am sorry, I don't have access to email."

---

## 3. Resilience Testing

### Test 1: The "Impossible Task"
1.  Ask: "Fly me to the moon."
2.  **Expectation**: The agent searches for tools, fails to find a flight tool, and responds "I cannot do that." It should NOT crash or loop infinitely.

### Test 2: Ollama Down
1.  Stop Ollama service.
2.  Run Agent.
3.  **Expectation**: Clean `ConnectionError` with a message: "Ensure Ollama serve is running on port 11434."
