import sys
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from langchain_core.messages import HumanMessage
from app.agent import get_agent_executor

console = Console()

def main():
    console.print(Panel.fit("[bold blue]🚀 Local AI Agent (A2) Initialized[/bold blue]\n[italic]Powered by LangChain & Ollama/OpenAI[/italic]", title="System"))
    console.print("[dim]Type 'exit' or 'quit' to stop.[/dim]\n")
    
    session_id = "test_session_v1"
    
    try:
        agent = get_agent_executor()
    except Exception as e:
        console.print(f"[bold red]❌ Failed to initialize agent:[/bold red] {e}")
        return

    while True:
        try:
            user_input = Prompt.ask("[bold green]User[/bold green]")
            if user_input.lower() in ["exit", "quit"]:
                console.print("[yellow]Exiting...[/yellow]")
                break
            
            with console.status("[bold cyan]Agent is reasoning...[/bold cyan]", spinner="dots"):
                response = agent.invoke(
                    {"messages": [HumanMessage(content=user_input)]},
                    config={"configurable": {"session_id": session_id}}
                )
            
            # Extract the last message content
            if isinstance(response, dict) and "messages" in response:
                last_message = response["messages"][-1]
                content = last_message.content
                console.print(Panel(Markdown(content), title="[bold blue]Agent[/bold blue]", expand=False))
            else:
                console.print(Panel(str(response), title="[bold blue]Agent[/bold blue]"))
                
        except KeyboardInterrupt:
            console.print("\n[yellow]Exiting...[/yellow]")
            break
        except Exception as e:
            if "Connection refused" in str(e) or "Error connecting" in str(e):
                console.print(f"\n[bold red]❌ Connection Error:[/bold red] {e}")
                console.print("Please ensure Ollama is running ('ollama serve') and Redis is up ('docker-compose up -d').")
                break
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
