from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return a list of tools to be used in the agentic AI graph.
    """

    tools=[TavilySearch(max_results=3)]
    return tools

def create_tool_node(tools):
    """
    Create a tool node for the agentic AI graph and return ToolNode instance.
    """
    return ToolNode(tools=tools)