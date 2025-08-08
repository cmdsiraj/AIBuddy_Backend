# from .LLMAgent.MyAgent.Agent.MyAgent import Agent
from .LLMAgent.MyAgent.Agent.MyAgent import Agent
from .LLMAgent.MyAgent.LLM.GeminiLLM import GeminiLLM
from .LLMAgent.MyAgent.Tools.ScraperTool import ScraperTool
from .LLMAgent.MyAgent.Tools.PdfHandlerTool import PdfHandlerTool
from .LLMAgent.MyAgent.Tools.SerperTool import SerperTool
from .LLMAgent.MyAgent.Tools.ExecutePythonTool import ExecutePythonTool
from .LLMAgent.MyAgent.utils.load_config import load_aget_config

llm = GeminiLLM(model_name="gemini-2.5-flash")
config = load_aget_config()

model = Agent (
    role=config["agent"]["role"],
    goal=config["agent"]["goal"],
    back_story=config["agent"]["back_story"],
    llm=llm,
    tools=[SerperTool(show_tool_call=True), ScraperTool(show_tool_call=True), PdfHandlerTool(show_tool_call=True), ExecutePythonTool(show_tool_call=True)],
    timeout=0,
)

def getResponse(message: str):
    response = model.chat(message)
    return response
