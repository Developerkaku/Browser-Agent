from browser_use import Agent, Browser, ChatGoogle
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    task="open lmarena web site, if it asks to sign wait bbruntill i sign in, if does not then continue, ater opening the site give the ai in the web site a prompt asking what version is it using , what are it's capabilities and let user take control",
    llm=ChatGoogle(model="gemini-flash-latest"),
    # browser=Browser(use_cloud=True),  # Uses Browser-Use cloud for the browser
)
agent.run_sync()