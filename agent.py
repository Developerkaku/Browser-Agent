from browser_use import Agent, Browser, ChatGoogle
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    task="open youtube",
    llm=ChatGoogle(model="gemini-flash-latest"),
    # browser=Browser(use_cloud=True),  # Uses Browser-Use cloud for the browser
)
agent.run_sync()