from .web_search import WebSearchTool
from .time_tool import TimeTool
from .base import ToolResult


class ToolManager:
    """Manages tool routing based on query keywords."""
    
    def __init__(self):
        self.web_search = WebSearchTool()
        self.time_tool = TimeTool()
        
        # Tool keywords mapping
        self.tool_keywords = {
            "web_search": [
                "search",
                "google",
                "internet",
                "web",
                "look up",
                "find",
                "latest",
                "news",
                "current",
            ],
            "time_tool": [
                "time",
                "date",
                "what time",
                "what date",
                "what's the time",
                "what's the date",
            ]
        }
    
    def route(self, query: str) -> ToolResult | None:
        """Route query to appropriate tool based on keywords."""
        query_lower = query.lower()
        
        # Check for time/date queries first (more specific)
        if any(keyword in query_lower for keyword in self.tool_keywords["time_tool"]):
            return self.time_tool.execute(query)
        
        # Check for web search queries
        if any(keyword in query_lower for keyword in self.tool_keywords["web_search"]):
            return self.web_search.execute(query)
        
        # No tool matched
        return None
