import sys
from io import StringIO
from app.agent import get_agent_executor
from langchain_core.messages import HumanMessage

def verify_agent():
    print("🧪 Verifying Agent Logic (Non-Interactive)...")
    
    agent = get_agent_executor()
    session_id = "verification_session"
    
    # Question that requires tool use (SQL)
    question = "How many orders are in the database?"
    print(f"❓ Question: {question}")
    
    try:
        response = agent.invoke(
            {"messages": [HumanMessage(content=question)]},
            config={"configurable": {"session_id": session_id}}
        )
        
        last_message = response["messages"][-1].content
        print(f"🤖 Answer: {last_message}")
        
        if "3" in last_message or "three" in last_message.lower():
            print("✅ Verification PASSED: Correct answer received.")
        else:
            print("⚠️ Verification WARNING: Answer might be incorrect (expected 3).")
            
    except Exception as e:
        print(f"❌ Verification FAILED: {e}")

if __name__ == "__main__":
    verify_agent()
